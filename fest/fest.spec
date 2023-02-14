# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit c7a5eb9ce1304d8f8a9935c99e98334221284d83
%global shortcommit c7a5eb9c

Name:    fest
Version: 1.0.2
Release: 1%{?dist}
Summary: Fixtures for Easy Software Testing

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:  0001-Remove-an-invalid-entity.patch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin) >= 2.1.2
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin) >= 2.8

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
Top-level pom metadata for FEST modules

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest

# Remove the assembly plugin.
# 1) Bundling dependencies is not the goal of RPM packages
# 2) The plugin definition uses the discouraged assembly:attached
# 3) These are all libraries, building an assembly jar doesn't even make sense
%pom_remove_plugin :maven-assembly-plugin

# don't want clover integration, and also it would require a license
%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin

# maven-site-plugin was retired from Fedora, and I don't care about it either
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin

# pom comes with source/target set to 1.5, update to something supported
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.7
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.7

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Feb 13 2023 David Shea <reallylongword@gmail.com> 1.2-1
- Initial package
