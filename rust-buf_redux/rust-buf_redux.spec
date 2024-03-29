# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate buf_redux

Name:           rust-buf_redux
Version:        0.8.4
Release:        3
Summary:        Drop-in replacements for buffered I/O in `std::io` with extra features

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/buf_redux
Source:         %{crates_source}

# The capacity checks fail on ppc64le due to the returned buffer being 64k instead of the capacity (8k or 4k) requested
Patch0:         buf_redux-minimum-alloc.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Drop-in replacements for buffered I/O in `std::io` with extra features.}

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
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+slice-deque-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+slice-deque-devel %{_description}

This package contains library source intended for building other packages which
use the "slice-deque" feature of the "%{crate}" crate.

%files       -n %{name}+slice-deque-devel
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
* Tue Jan 24 2023 David Shea <reallylongword@gmail.com> - 0.8.4-3
- Remove rpmautospec macros

* Sun Oct 16 2022 David Shea <reallylongword@gmail.com> - 0.8.4-2
- Disable the capacity checks

* Sun Oct 16 2022 David Shea <reallylongword@gmail.com> - 0.8.4-1
- Initial package
