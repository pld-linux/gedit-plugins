Summary:	gedit plugins
Summary(pl):	Wtyczki dla gedita
Name:		gedit-plugins
Version:	2.15.3
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/gnome/sources/gedit-plugins/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	4182e0b3b522cb35e5348ce00c8aaa1d
Patch0:		%{name}-configure.patch
URL:		http://gedit.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gedit2-devel >= 2.3.5
BuildRequires:	glib2-devel >= 1:2.11.2
BuildRequires:	gucharmap-devel >= 1.6.0
BuildRequires:	intltool >= 0.35
BuildRequires:	libtool
BuildRequires:	python-gnome-desktop-devel >= 2.15.2
BuildRequires:	rpm-build >= 4.1-10
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	gedit2 >= 2.15.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of plugins for gedit.

%description -l pl
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
	--enable-python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove obsoleted *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*.{la,py}

#%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gedit-show-tabbar-plugin.schemas

%preun
%gconf_schema_uninstall gedit-show-tabbar-plugin.schemas

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/gedit-2/plugins/*.so*
%{_libdir}/gedit-2/plugins/*.gedit-plugin
%{_libdir}/gedit-2/plugins/*.py[co]
%{_sysconfdir}/gconf/schemas/gedit-show-tabbar-plugin.schemas
