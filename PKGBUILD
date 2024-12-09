# Maintainer: Gianni Ferrarotti <gianni.ferrarotti@gmail.com>

pkgname=azadi-noweb
pkgver=0.1.2
pkgrel=1
pkgdesc="A Rust implementation of noweb-style literate programming tool"
url="https://github.com/giannifer7/$pkgname"
license=('MIT')
makedepends=('cargo')
depends=()
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
source=("$pkgname-$pkgver.tar.gz::https://github.com/giannifer7/$pkgname/archive/v$pkgver.tar.gz")
sha512sums=('83b233803953a3f7ed7f6064e3269a24da8127b7e14e7cf16b0b4826ded369b0152dbeadc829d957756040581724d30c419774a92f2660b18b3ec118ddc0c904')

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
