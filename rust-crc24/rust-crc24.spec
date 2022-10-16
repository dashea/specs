# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate crc24

Name:           rust-crc24
Version:        0.1.6
Release:        %autorelease
Summary:        CRC-24 implementation (IETF RFC2440-compatible)

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crc24
Source0:        %{crates_source}

# Use license files from upstream git
# The commit ID is arbitrary, just to ensure the content/existence of the files doesn't change
Source1:        https://raw.githubusercontent.com/sellibitze/crc24-rs/521ddbbe1909c06fe322a06b00de1260c5d3acd6/LICENSE-APACHE
Source2:        https://raw.githubusercontent.com/sellibitze/crc24-rs/521ddbbe1909c06fe322a06b00de1260c5d3acd6/LICENSE-MIT

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
CRC-24 implementation (IETF RFC2440-compatible).}

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

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
cp "%{SOURCE1}" .
cp "%{SOURCE2}" .
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