Summary:	gedit plugins
Summary(pl.UTF-8):   Wtyczki dla gedita
Name:		gedit-plugins
Version:	2.17.2
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/gnome/sources/gedit-plugins/2.17/%{name}-%{version}.tar.bz2
# Source0-md5:	b8c0f762e1cc306c807a4937c88050f7
URL:		http://gedit.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	gedit2-devel >= 2.17.6
BuildRequires:	glib2-devel >= 1:2.12.9
BuildRequires:	gucharmap-devel >= 1.8.0
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	python-gnome-desktop-devel >= 2.17.93
BuildRequires:	python-vte >= 0.15.6
BuildRequires:	rpm-build >= 4.1-10
Requires(post,preun):	GConf2
Requires:	gedit2 >= 2.17.6
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
%dir %{_libdir}/gedit-2/plugins/sessionsaver
%{_libdir}/gedit-2/plugins/sessionsaver/sessionsaver.glade
%{_libdir}/gedit-2/plugins/sessionsaver/*.py[co]
%{_sysconfdir}/gconf/schemas/gedit-show-tabbar-plugin.schemas
