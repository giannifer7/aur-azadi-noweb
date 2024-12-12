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
sha512sums=('a335a83cb68bb72c2277f3011bbc0d0a8a6a5dadce1df9feea81af194549b8842d095fbae50c266b1e50fa2ba2e60bfb968c3babfe236f3e3737011d7b7e5f3e')

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
