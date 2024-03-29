# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate sha2

Name:           rust-sha2_0.8
Version:        0.8.2
Release:        2
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sha2
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Pure Rust implementation of the SHA-2 hash function family including SHA-224,
SHA-256, SHA-384, and SHA-512.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license LICENSE-APACHE
%license LICENSE-MIT
%doc CHANGELOG.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+asm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+asm-devel %{_description}

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%files       -n %{name}+asm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+asm-aarch64-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+asm-aarch64-devel %{_description}

This package contains library source intended for building other packages which
use the "asm-aarch64" feature of the "%{crate}" crate.

%files       -n %{name}+asm-aarch64-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compress-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compress-devel %{_description}

This package contains library source intended for building other packages which
use the "compress" feature of the "%{crate}" crate.

%files       -n %{name}+compress-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sha2-asm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sha2-asm-devel %{_description}

This package contains library source intended for building other packages which
use the "sha2-asm" feature of the "%{crate}" crate.

%files       -n %{name}+sha2-asm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Jan 24 2023 David Shea <reallylongword@gmail.com> - 0.8.2-2
- Remove rpmautospec macros

* Sun Oct 16 2022 David Shea <reallylongword@gmail.com> - 0.8.2-1
- Initial package
