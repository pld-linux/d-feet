Summary:	D-Feet - a D-Bus debugger
Name:		d-feet
Version:	0.1.10
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://johnp.fedorapeople.org/downloads/d-feet/%{name}-%{version}.tar.gz
# Source0-md5:	c97df997442a99233229d45bff5ed88d
URL:		https://fedorahosted.org/d-feet/
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Requires:	python-dbus
Requires:	python-pygtk-gtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-Feet is a D-Bus debugger.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/d-feet
%{_desktopdir}/dfeet.desktop
%{py_sitescriptdir}/dfeet
%{py_sitescriptdir}/d_feet-%{version}-py*.egg-info
%{_datadir}/dfeet
%{_iconsdir}/hicolor/*/apps/dfeet*.png
