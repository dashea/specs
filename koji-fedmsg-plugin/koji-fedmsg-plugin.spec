%global commit 52ace3599c7ae35069542e6d56a46925af9d250c
%global shortcommit 52ace35

Name:           koji-fedmsg-plugin
Version:        0.1.0^20220713git%{shortcommit}
Release:        1%{?dist}
Summary:        Koji plugin to send messages on fedora-messaging

License:        GPLv3+
URL:            https://pagure.io/koji-fedmsg-plugin

# The upstream source has not tagged a release, and Pagure does not allow downloading
# archives of arbitrary commits. Rehost on github so it can be downloaded.
Source0: https://github.com/dashea/koji-fedmsg-plugin/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# From https://pagure.io/koji-fedmsg-plugin/pull-request/18
Patch0:  0001-Handle-long-data-type-in-koji-fedmsg-plugin.py.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A koji plugin to send message on fedora-messaging.}

%description %_description

%package -n python3-koji-fedmsg-plugin
Summary:        %{summary}

%description -n python3-koji-fedmsg-plugin %_description


%prep
%autosetup -p1 -n koji-fedmsg-plugin-%{commit}
# This is the one file that actually counts. It's not part of the python module and should not be treated as such.
mv koji_fedmsg_plugin/koji-fedmsg-plugin.py .

# Don't package the tests with the module
mv koji_fedmsg_plugin/tests .

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

PYTHONPATH="$PWD" make -C docs html


%install
%pyproject_install

%pyproject_save_files koji_fedmsg_plugin

install -D -m 0644 koji-fedmsg-plugin.py %{buildroot}%{_prefix}/lib/koji-hub-plugins/fedmsg.py


%check
%pytest

%files
%license COPYING
%{_prefix}/lib/koji-hub-plugins/fedmsg.py


%files -n python3-koji-fedmsg-plugin -f %{pyproject_files}
%license COPYING
%doc README.md TODO.md docs/build/html

%changelog
* Fri Oct 21 2022 David Shea <reallylongword@gmail.com> - 0.1.0^20220713git52ace35-1
- Initial package
