# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate num-complex

Name:           rust-num-complex0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Complex numbers implementation for Rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num-complex
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Complex numbers implementation for Rust.}

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
