# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate cfb-mode

Name:           rust-cfb-mode0.6
Version:        0.6.0
Release:        2
Summary:        Generic Cipher Feedback (CFB) mode implementation

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cfb-mode
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Generic Cipher Feedback (CFB) mode implementation.}

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
* Tue Jan 24 2023 David Shea <reallylongword@gmail.com> - 0.6.0-2
- Remove rpmautospec macros

* Sun Oct 16 2022 David Shea <reallylongword@gmail.com> - 0.6.0-1
- Initial package
