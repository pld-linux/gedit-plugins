Summary:	gedit plugins
Summary(pl.UTF-8):	Wtyczki dla gedita
Name:		gedit-plugins
Version:	2.32.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gedit-plugins/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	b5123846fa41f2d94992ae67e96ff79b
Patch0:		%{name}-codegen.patch
URL:		http://www.gnome.org/projects/gedit/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	gedit2-devel >= 2.30.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gtksourceview2-devel >= 2.10.0
BuildRequires:	gucharmap-devel >= 2.24.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-dbus-devel >= 0.82
BuildRequires:	python-gtksourceview2-devel >= 2.10.0
BuildRequires:	python-pygobject-devel >= 2.16.0
BuildRequires:	python-pygtk-devel >= 2:2.14.0
BuildRequires:	python-vte-devel >= 0.20.0
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
Requires(post,preun):	GConf2
Requires:	gedit2 >= 2.30.0
Requires:	gtksourceview2 >= 2.10.0
Requires:	python-dbus >= 0.82
Requires:	python-gnome-gconf >= 2.22.0
Requires:	python-gnome-vfs >= 2.22.0
Requires:	python-pygobject >= 2.16.0
Requires:	python-pygtk-glade >= 2:2.14.0
Requires:	python-pygtk-gtk >= 2:2.14.0
Requires:	python-vte >= 0.20.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of plugins for gedit.

%description -l pl.UTF-8
Zestaw wtyczek dla gedita.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove not needed files
rm -f $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*.la

%py_postclean %{_libdir}/gedit-2/plugins

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gedit-drawspaces.schemas
%gconf_schema_install gedit-show-tabbar-plugin.schemas

%preun
%gconf_schema_uninstall gedit-drawspaces.schemas
%gconf_schema_uninstall gedit-show-tabbar-plugin.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/gedit-2/plugins/libbookmarks.so
%attr(755,root,root) %{_libdir}/gedit-2/plugins/libcharmap.so
%attr(755,root,root) %{_libdir}/gedit-2/plugins/libdrawspaces.so
%attr(755,root,root) %{_libdir}/gedit-2/plugins/libshowtabbar.so
%attr(755,root,root) %{_libdir}/gedit-2/plugins/libwordcompletion.so
%{_libdir}/gedit-2/plugins/bookmarks.gedit-plugin
%{_libdir}/gedit-2/plugins/bracketcompletion.gedit-plugin
%{_libdir}/gedit-2/plugins/bracketcompletion.py[co]
%{_libdir}/gedit-2/plugins/charmap.gedit-plugin
%{_libdir}/gedit-2/plugins/codecomment.gedit-plugin
%{_libdir}/gedit-2/plugins/codecomment.py[co]
%{_libdir}/gedit-2/plugins/colorpicker.gedit-plugin
%{_libdir}/gedit-2/plugins/colorpicker.py[co]
%{_libdir}/gedit-2/plugins/commander.gedit-plugin
%dir %{_libdir}/gedit-2/plugins/commander
%{_libdir}/gedit-2/plugins/commander/*.py[co]
%dir %{_libdir}/gedit-2/plugins/commander/commands
%{_libdir}/gedit-2/plugins/commander/commands/*.py[co]
%{_libdir}/gedit-2/plugins/drawspaces.gedit-plugin
%{_libdir}/gedit-2/plugins/gpdefs.py[co]
%{_libdir}/gedit-2/plugins/joinlines.gedit-plugin
%{_libdir}/gedit-2/plugins/joinlines.py[co]
%{_libdir}/gedit-2/plugins/multiedit.gedit-plugin
%dir %{_libdir}/gedit-2/plugins/multiedit
%{_libdir}/gedit-2/plugins/multiedit/*.py[co]
%{_libdir}/gedit-2/plugins/sessionsaver.gedit-plugin
%{_libdir}/gedit-2/plugins/showtabbar.gedit-plugin
%{_libdir}/gedit-2/plugins/smartspaces.gedit-plugin
%{_libdir}/gedit-2/plugins/smartspaces.py[co]
%{_libdir}/gedit-2/plugins/synctex.gedit-plugin
%dir %{_libdir}/gedit-2/plugins/synctex
%{_libdir}/gedit-2/plugins/synctex/*.py[co]
%{_libdir}/gedit-2/plugins/terminal.gedit-plugin
%{_libdir}/gedit-2/plugins/terminal.py[co]
%{_libdir}/gedit-2/plugins/textsize.gedit-plugin
%dir %{_libdir}/gedit-2/plugins/textsize
%{_libdir}/gedit-2/plugins/textsize/*.py[co]
%dir %{_libdir}/gedit-2/plugins/sessionsaver
%{_libdir}/gedit-2/plugins/sessionsaver/*.py[co]
%{_libdir}/gedit-2/plugins/wordcompletion.gedit-plugin
%{_sysconfdir}/gconf/schemas/gedit-drawspaces.schemas
%{_sysconfdir}/gconf/schemas/gedit-show-tabbar-plugin.schemas
%{_datadir}/gedit-2/plugins/bookmarks
%{_datadir}/gedit-2/plugins/commander
%{_datadir}/gedit-2/plugins/drawspaces
%{_datadir}/gedit-2/plugins/sessionsaver
