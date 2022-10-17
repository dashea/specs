# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate num-bigint-dig

Name:           rust-num-bigint-dig0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Big integer implementation for Rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num-bigint-dig
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Big integer implementation for Rust.}

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
%doc README.md
%doc RELEASES.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+i128-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+i128-devel %{_description}

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

%files       -n %{name}+i128-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prime-devel %{_description}

This package contains library source intended for building other packages which
use the "prime" feature of the "%{crate}" crate.

%files       -n %{name}+prime-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+u64_digit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+u64_digit-devel %{_description}

This package contains library source intended for building other packages which
use the "u64_digit" feature of the "%{crate}" crate.

%files       -n %{name}+u64_digit-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zeroize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zeroize-devel %{_description}

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

%files       -n %{name}+zeroize-devel
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
%autochangelog
