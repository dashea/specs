Name:    python-yq
Version: 3.1.0
Release: 1%{?dist}
Summary: jq wrapper for YAML, XML, TOML documents

License: ASL 2.0
URL:     https://github.com/kislyuk/yq
Source0: %{pypi_source yq}

Patch0:  0001-Do-no-automatically-install-test-deps.patch
Patch1:  0002-Use-versioned-python-executable.patch

BuildArch: noarch

BuildRequires: python3-devel

# Test and doc requirements
BuildRequires: make
BuildRequires: %{py3_dist flake8}
BuildRequires: %{py3_dist coverage}
BuildRequires: /usr/bin/jq
BuildRequires: %{py3_dist guzzle-sphinx-theme}
BuildRequires: /usr/bin/sphinx-build

%global _description %{expand:
yq takes YAML input, converts it to JSON, and pipes it to jq.

yq also supports XML. The yq package installs an executable, xq, which
transcodes XML to JSON using xmltodict and pipes it to jq. Roundtrip
transcoding is available with the xq --xml-output/xq -x option.

yq supports TOML as well. The yq package installs an executable, tomlq, which
uses the toml library to transcode TOML to JSON, then pipes it to jq. Roundtrip
transcoding is available with the tomlq --toml-output/tomlq -t option.}

%description %_description

%package -n python3-yq
Summary: %{summary}

Requires: /usr/bin/jq

%description -n python3-yq %_description

%prep
%autosetup -n yq-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

make docs

%install
%pyproject_install
%pyproject_save_files yq

%check
make test

%files -n python3-yq -f %{pyproject_files}
%doc Changes.rst README.rst docs/html
%license LICENSE
%{_bindir}/yq
%{_bindir}/xq
%{_bindir}/tomlq

%changelog
* Fri Oct 21 2022 David Shea <reallylongword@gmail.com> - 3.1.0-1
- Initial package
