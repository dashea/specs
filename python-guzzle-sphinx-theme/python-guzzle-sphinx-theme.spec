Name:    python-guzzle-sphine-theme
Version: 0.7.11
Release: 1%{?dist}
Summary: Sphinx theme used by Guzzle

License: MIT
URL:     https://github.com/guzzle/guzzle_sphinx_theme
Source0: %{pypi_source guzzle_sphinx_theme}

BuildArch: noarch

BuildRequires: python3-devel

%global _description %{expand:
Sphinx theme used by guzzle: Sphinx theme used by Guzzle: http://guzzlephp.org}

%description %_description

%package -n python3-guzzle-sphinx-theme
Summary: %{summary}

%description -n python3-guzzle-sphinx-theme %_description

%prep
%autosetup -n guzzle_sphinx_theme-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files guzzle_sphinx_theme

%files -n python3-guzzle-sphinx-theme -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Fri Oct 21 2022 David Shea <reallylongword@gmail.com> - 0.7.11-1
- Initial package
