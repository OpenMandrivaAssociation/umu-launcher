%undefine _debugsource_packages
Name:           umu-launcher
Version:        1.4.0
Release:        1
Group:          Games
Summary:        A tool for launching non-steam games with proton
License:        GPL-3.0-only
URL:            https://github.com/Open-Wine-Components/umu-launcher
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  make
BuildRequires:  scdoc
BuildRequires:  cargo
BuildRequires:  python
BuildRequires:  python-build
BuildRequires:  python-hatchling
BuildRequires:  python-installer
BuildRequires:  python-devel
BuildRequires:  python-urllib3
BuildRequires:  python-xlib
BuildRequires:  python-zstd
BuildRequires:  python-xxhash
BuildRequires:  python-cbor2
BuildRequires:  python-devel

Requires:       python
Requires:       python-xlib
Requires:       python%{pyver}dist(urllib3)
Requires:       python%{pyver}dist(xxhash)
Requires:       python%{pyver}dist(zstd)
Requires:       python%{pyver}dist(cbor2)

%description
%summary

%prep
%autosetup -p1

%build
./configure.sh --prefix=%{_prefix} --use-system-pyzstd --use-system-urllib
%make_build UMU_VERSION=%{version}

%install
%make_install PYTHONDIR=%{python3_sitelib} UMU_VERSION=%{version} DESTDIR=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/umu-run
%{_datadir}/man/*
%{python3_sitelib}/umu*
