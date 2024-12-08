from pathlib import Path

import argparse


def pkgbuild_template(pkgname, pkgver, sha512sum, user):
    return (
        f"""\
# Maintainer: {user["name"]} <{user["email"]}>

pkgname={pkgname}
pkgver={pkgver}
pkgrel=1
pkgdesc="A Rust implementation of noweb-style literate programming tool"
url="https://github.com/{user['ghname']}/$pkgname"
license=('MIT')
makedepends=('cargo')
depends=()
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
source=("$pkgname-$pkgver.tar.gz::https://github.com/{user['ghname']}/$pkgname/archive/v$pkgver.tar.gz")
sha512sums=('{sha512sum}')
"""
        """
prepare() {
    cd "$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
    cd "$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --frozen --release --all-features
}

check() {
    cd "$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    cargo test --frozen --all-features
}

package() {
    cd "$pkgname-$pkgver"
    install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
"""
    )


def main() -> None:
    argp = argparse.ArgumentParser(
        prog="mkPKGBUILD",
        description=(
            "generate PKGBUILD from a template, given pkgname, pkgver and the sha512sum file"
        ),
    )
    argp.add_argument("pkgname", help="pkgname to be substituted in the template")
    argp.add_argument("pkgver", help="pkgver to be substituted in the template")
    argp.add_argument("sha512sum_filename", help="filename of the sha512 checksum")

    args = argp.parse_args()

    sha_path = Path(args.sha512sum_filename)
    sha512sum = sha_path.read_text().split(maxsplit=1)[0]

    user = {
        "name": "Gianni Ferrarotti",
        "email": "gianni.ferrarotti@gmail.com",
        "ghname": "giannifer7",
    }

    pkgbuild = pkgbuild_template(args.pkgname, args.pkgver, sha512sum, user)
    this_dir = Path(__file__).parent.resolve()

    out_filename = this_dir / "PKGBUILD"
    out_filename.write_text(pkgbuild)
    print(f"{out_filename} generated.")


if __name__ == "__main__":
    main()
