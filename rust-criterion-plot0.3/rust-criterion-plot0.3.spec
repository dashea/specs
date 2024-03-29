# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate criterion-plot

Name:           rust-criterion-plot0.3
Version:        0.3.1
Release:        2
Summary:        Criterion's plotting library

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/criterion-plot
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Criterion's plotting library.}

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
%doc CONTRIBUTING.md
%doc README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# Crate has a ton of inapporiate executable bits
find . -type f | xargs chmod -x
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
* Tue Jan 24 2023 David Shea <reallylongword@gmail.com> - 0.3.1-2
- Remove rpmautospec macros

* Sun Oct 16 2022 David Shea <reallylongword@gmail.com> - 0.3.1-1
- Initial package
