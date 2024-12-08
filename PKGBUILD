# Maintainer: Gianni Ferrarotti <gianni.ferrarotti@gmail.com>

pkgname=azadi-noweb
pkgver=0.1.1
pkgrel=1
pkgdesc="A Rust implementation of noweb-style literate programming tool"
url="https://github.com/giannifer7/$pkgname"
license=('MIT')
makedepends=('cargo')
depends=()
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
source=("$pkgname-$pkgver.tar.gz::https://github.com/giannifer7/$pkgname/archive/v$pkgver.tar.gz")
sha512sums=('f26f5245401f5b3e56933e76c22cda2d698a1b2ba753541298724d08447762b9a7f8e7cd4886f826a3666b94dfaef9e42da4296d49b1b578a9789933a0fe7cfa')

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
