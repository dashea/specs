# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit 23774b239e4c3f0a65f32910ed540f5f1a8f9c78
%global shortcommit 23774b239

Name:    fest-util
Version: 1.1.4
Release: 1%{?dist}
Summary: FEST Util

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit) >= 4.7

Requires: java-headless
Requires: javapackages-filesystem

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
Utility methods used by FEST modules

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest-util

# Allow newer versions of junit
%pom_change_dep junit:junit:4.7 junit:junit:any

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%changelog
* Mon Feb 13 2023 David Shea <reallylongword@gmail.com> 1.2-1
- Initial package
