# Maintainer: Gianni Ferrarotti <gianni.ferrarotti@gmail.com>

pkgname=azadi-noweb
pkgver=1.0.0
pkgrel=1
pkgdesc="A Rust implementation of noweb-style literate programming tool"
url="https://github.com/giannifer7/azadi-noweb"
license=('MIT')
makedepends=('cargo')
depends=()
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
source=("$pkgname-$pkgver.tar.gz::https://github.com/giannifer7/$pkgname/archive/v$pkgver.tar.gz")
sha512sums=('5270a8f9c9f69f35fa9554e6b99af9cf8bfa18ca3f0bd47ed8e6506f843fec2fb28d24af99c34a793ee1f8d74caf5e970921b95d3f633df0d7abf6af3f41392a')

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
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
