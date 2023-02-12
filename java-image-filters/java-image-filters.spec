Name:    java-image-filters
Version: 2.0.235
Release: 1%{?dist}
Summary: Java image filters

License: Apache-2.0
URL:     http://www.jhlabs.com/ip/filters/
Source0: http://www.jhlabs.com/ip/filters/Filters.zip

# Referenced in all source headers but not included in the source dist
Source1: LICENSE-2.0.txt

# project is on mvn repository but doesn't ship a pom.xml
Source2: https://repo1.maven.org/maven2/com/jhlabs/filters/2.0.235/filters-2.0.235.pom

BuildRequires: ant
BuildRequires: maven-local
Requires: java-headless
Requires: javapackages-filesystem

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
The filters are all standard Java BufferedImageOps and can be plugged directly
into existing programs. All the filters are available in the Java Image Editor
and most have dialogs to allow you to play with their settings.

%prep
%autosetup -c

find . -name '*.jar' | xargs rm

cp %{SOURCE1} .
cp %{SOURCE2} pom.xml

%build
ant

%install
%mvn_artifact pom.xml dist/Filters.jar
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt

%changelog
* Sun Feb 12 2023 David Shea <reallylongword@gmail.com> - 2.0.235-1
- Initial package
