#
# Conditional build:
%bcond_without	tests	# test suite
#
Summary:	D-Feet - a D-Bus debugger
Summary(pl.UTF-8):	D-Feet - debugger dla magistrali D-Bus
Name:		d-feet
Version:	0.3.16
Release:	5
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/d-feet/0.3/%{name}-%{version}.tar.xz
# Source0-md5:	c5cc09323c725210b0c420e40fb81e4c
Patch0:		%{name}-cleanup.patch
Patch1:		meson0.60.patch
URL:		https://wiki.gnome.org/Apps/DFeet
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.5
%{?with_tests:BuildRequires:	python3-pep8}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2-devel >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gtk+3 >= 3.10
Requires:	python3 >= 1:3.5
Requires:	python3-pygobject3 >= 3.4
Suggests:	libwnck >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-Feet is a D-Bus debugger.

%description -l pl.UTF-8
D-Feet to debugger dla magistrali D-Bus.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%build
%meson \
	%{!?with_tests:-Dtests=false}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}

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
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/d-feet
%{_datadir}/d-feet
%{_datadir}/glib-2.0/schemas/org.gnome.dfeet.gschema.xml
%{_datadir}/metainfo/org.gnome.dfeet.appdata.xml
%{py3_sitescriptdir}/dfeet
%{_desktopdir}/org.gnome.dfeet.desktop
%{_iconsdir}/hicolor/16x16/apps/dfeet-*.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.dfeet.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.dfeet-symbolic.svg
