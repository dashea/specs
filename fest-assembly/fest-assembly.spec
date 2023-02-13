# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit c7a5eb9ce1304d8f8a9935c99e98334221284d83
%global shortcommit c7a5eb9c

Name:    fest-assembly
Version: 1.0
Release: 1%{?dist}
Summary: Fixtures for Easy Software Testing: shared assembly descriptor

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: maven-local

Requires: java-headless
Requires: javapackages-filesystem

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
Shared assembly descriptor for FEST modules

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest-assembly

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Feb 13 2023 David Shea <reallylongword@gmail.com> 1.2-1
- Initial package
