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
sha512sums=('0481bf6b15d1a14b1cff7f8e8df6a5b203a057b9508e5429389cf9b1f7681f8b4135ae5969486e40920a53e8ddf98b8e176f15db8530e335db73f36ea493be16')

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
