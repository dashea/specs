# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit 323f98e25ce07028f55330f25753438818ecab74
%global shortcommit 323f98e2

Name:    fest-test
Version: 1.2.1
Release: 1%{?dist}
Summary: FEST Testing

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.easytesting:fest:pom:) >= 1.0.1
BuildRequires: mvn(org.easytesting:fest-util) >= 1.1.2
BuildRequires: mvn(junit:junit) >= 4.7

Requires: mvn(org.easytesting:fest:pom:)

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
Utility methods for testing FEST modules

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest-test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Feb 14 2023 David Shea <reallylongword@gmail.com> 1.2.1-1
- Initial package
