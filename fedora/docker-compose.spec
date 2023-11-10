Name:           docker-compose
Version:        1.29.3
Release:        %autorelease
Summary:        Multi-container orchestration for Docker
License:        ASL 2.0
URL:            https://github.com/TomasTomecek/fedora-docker-compose
Source:         https://github.com/TomasTomecek/fedora-docker-compose/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-distro
BuildRequires:  python%{python3_pkgversion}-dotenv
BuildRequires:  python%{python3_pkgversion}-ddt

BuildRequires:  python%{python3_pkgversion}-cached_property >= 1.5.1
BuildRequires:  python%{python3_pkgversion}-chardet >= 3.0.4
BuildRequires:  python%{python3_pkgversion}-distro >= 1.5.0
BuildRequires:  python%{python3_pkgversion}-docker >= 5.0.0
BuildRequires:  python%{python3_pkgversion}-docker-pycreds >= 0.4.0
BuildRequires:  python%{python3_pkgversion}-dockerpty >= 0.4.1
BuildRequires:  python%{python3_pkgversion}-docopt >= 0.6.2
BuildRequires:  python%{python3_pkgversion}-idna >= 2.10
BuildRequires:  python%{python3_pkgversion}-jsonschema >= 3.2.0
BuildRequires:  python%{python3_pkgversion}-pysocks >= 1.7.1
BuildRequires:  python%{python3_pkgversion}-requests >= 2.24.0
BuildRequires:  python%{python3_pkgversion}-six >= 1.12.0
BuildRequires:  python%{python3_pkgversion}-texttable >= 1.6.2
BuildRequires:  python%{python3_pkgversion}-websocket-client >= 0.57.0
BuildRequires:  python%{python3_pkgversion}-yaml >= 5.4.1

Requires:       python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}-cached_property >= 1.5.1
Requires:       python%{python3_pkgversion}-chardet >= 3.0.4
Requires:       python%{python3_pkgversion}-distro >= 1.5.0
Requires:       python%{python3_pkgversion}-docker >= 5.0.0
Requires:       python%{python3_pkgversion}-docker-pycreds >= 0.4.0
Requires:       python%{python3_pkgversion}-dockerpty >= 0.4.1
Requires:       python%{python3_pkgversion}-docopt >= 0.6.2
Requires:       python%{python3_pkgversion}-idna >= 2.10
Requires:       python%{python3_pkgversion}-jsonschema >= 3.2.0
Requires:       python%{python3_pkgversion}-pysocks >= 1.7.1
Requires:       python%{python3_pkgversion}-requests >= 2.24.0
Requires:       python%{python3_pkgversion}-six >= 1.12.0
Requires:       python%{python3_pkgversion}-texttable >= 1.6.2
Requires:       python%{python3_pkgversion}-websocket-client >= 0.57.0
Requires:       python%{python3_pkgversion}-yaml >= 5.4.1

Requires:       python%{python3_pkgversion}-attrs >= 20.3.0
Requires:       python%{python3_pkgversion}-certifi >= 2020.6.20


%description
Compose is a tool for defining and running multi-container Docker
applications. With Compose, you use a Compose file to configure your
application's services. Then, using a single command, you create and
start all the services from your configuration.

Compose is great for development, testing, and staging environments,
as well as CI workflows.

Using Compose is basically a three-step process.

1. Define your app's environment with a Dockerfile so it can be
   reproduced anywhere.
2. Define the services that make up your app in docker-compose.yml so
   they can be run together in an isolated environment:
3. Lastly, run docker-compose up and Compose will start and run your
   entire app.


%prep
%autosetup -p 1
rm -rf docker_compose.egg-info

# Remove dependency version constraints not relevant in Fedora/EPEL
sed -e 's/, < [0-9.]\+//' -i setup.py


%build
%py3_build


%install
%py3_install
install -D -p -m 644 contrib/completion/bash/docker-compose %{buildroot}%{_datadir}/bash-completion/completions/docker-compose
install -D -p -m 644 contrib/completion/zsh/_docker-compose %{buildroot}%{_datadir}/zsh/site-functions/_docker-compose
install -D -p -m 644 contrib/completion/fish/docker-compose.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/docker-compose.fish


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} --verbose tests/unit


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{python3_sitelib}/compose
%{python3_sitelib}/docker_compose-%{version}-py%{python3_version}.egg-info
%{_datadir}/bash-completion
%{_datadir}/zsh
%{_datadir}/fish


%changelog
%autochangelog
