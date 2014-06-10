#
# Conditional build:
%bcond_without	tests	# test suite
#
Summary:	D-Feet - a D-Bus debugger
Summary(pl.UTF-8):	D-Feet - debugger dla magistrali D-Bus
Name:		d-feet
Version:	0.3.9
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/d-feet/0.3/%{name}-%{version}.tar.xz
# Source0-md5:	91da9520aa0460bdb51e60b93b61102f
URL:		http://live.gnome.org/DFeet/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.7
%{?with_tests:BuildRequires:	python-pep8}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
%pyrequires_eq	python-modules
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2-devel >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gtk+3 >= 3.10
Requires:	python >= 1:2.7
Requires:	python-pygobject3 >= 3.4
Suggests:	libwnck >= 3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-Feet is a D-Bus debugger.

%description -l pl.UTF-8
D-Feet to debugger dla magistrali D-Bus.

%prep
%setup -q

%build
# rebuild with POSIX sh compatible yelp macros
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_tests:--disable-tests}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/d-feet
%{_datadir}/d-feet
%{_datadir}/appdata/d-feet.appdata.xml
%{_desktopdir}/d-feet.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.d-feet.gschema.xml
%{py_sitescriptdir}/dfeet
%{_iconsdir}/hicolor/*/apps/d-feet.*
%{_iconsdir}/hicolor/16x16/apps/dfeet-*.png
# who owns top dir?
#%{_iconsdir}/HighContrast/scalable/apps/d-feet.svg
