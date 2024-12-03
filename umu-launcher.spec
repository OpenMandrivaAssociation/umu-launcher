%global apparmor_profile_name bwrap-userns-restrict
%if %{pkg_vcmp apparmor-profiles >= 4}
%bcond_with    apparmor4
%else
%bcond_with    apparmor4
%endif
Name:           umu-launcher
Version:        1.1.4
Release:        1
Group:          Games
Summary:        A tool for launching non-steam games with proton
License:        GPL-3.0-only
URL:            https://github.com/Open-Wine-Components/umu-launcher
Source0:        https://github.com/Open-Wine-Components/umu-launcher/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python-build
BuildRequires:  pkgconfig(python)
BuildRequires:  python-filelock
BuildRequires:  python-hatchling
BuildRequires:  python-installer
BuildRequires:  python-xlib
BuildRequires:  scdoc
BuildRequires:  zstd
Requires:       python
Requires:       python-filelock
Requires:       python-xlib
BuildArch:      noarch

%description
This is a unified launcher for Windows games on Linux. It is essentially a copy
of the Steam Runtime Tools and Steam Linux Runtime that Valve uses for Proton,
with some modifications made so that it can be used outside of Steam.

%prep
%autosetup -p1

%build
./configure.sh --prefix=%{_prefix}
%make_build UMU_VERSION=%{version}

%install
%make_install PYTHONDIR=%{python3_sitelib} UMU_VERSION=%{version}

%files
%license LICENSE
%doc README.md
%{_bindir}/umu-run
%{_mandir}/man*/umu*
%{python3_sitelib}/umu/
%{python3_sitelib}/umu_launcher-%{version}.dist-info
# TODO: should ensure it uses the same values as the steam package?
%dir %{_datadir}/steam/
%dir %{_datadir}/steam/compatibilitytools.d/
#/ TODO
%{_datadir}/steam/compatibilitytools.d/umu-launcher/