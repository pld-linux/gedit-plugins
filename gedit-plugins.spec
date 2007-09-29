Summary:	gedit plugins
Summary(pl.UTF-8):	Wtyczki dla gedita
Name:		gedit-plugins
Version:	2.20.0
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gedit-plugins/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	ec5be3d10ca4da4b33effad207ef35e9
URL:		http://www.gnome.org/projects/gedit/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	gedit2-devel >= 2.20.0
BuildRequires:	glib2-devel >= 1:2.14.1
BuildRequires:	gtksourceview2-devel >= 2.0.0
BuildRequires:	gucharmap-devel >= 1.10.0
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libtool
BuildRequires:	python-gnome-desktop-devel >= 2.20.0
BuildRequires:	python-vte >= 0.16.8
BuildRequires:	rpm-build >= 4.1-10
Requires(post,preun):	GConf2
Requires:	gedit2 >= 2.20.0
Requires:	python-gnome-desktop-gtksourceview >= 2.20.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of plugins for gedit.

%description -l pl.UTF-8
Zestaw wtyczek dla gedita.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove not needed files
rm -f $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*.{la,py}
rm -f $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/sessionsaver/*.py
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gedit-show-tabbar-plugin.schemas

%preun
%gconf_schema_uninstall gedit-show-tabbar-plugin.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/gedit-2/plugins/*.so*
%{_libdir}/gedit-2/plugins/*.gedit-plugin
%{_libdir}/gedit-2/plugins/*.py[co]
%{_libdir}/gedit-2/plugins/drawspaces.glade
%dir %{_libdir}/gedit-2/plugins/sessionsaver
%{_libdir}/gedit-2/plugins/sessionsaver/sessionsaver.glade
%{_libdir}/gedit-2/plugins/sessionsaver/*.py[co]
%{_sysconfdir}/gconf/schemas/gedit-show-tabbar-plugin.schemas
