Name:		htop
Version:	1.0.3
Release:	1%{?dist}
Summary:	htop

Group:		Applications/System
License:	GPL
URL:		http://hisham.hm/htop
Source0:	htop-1.0.3.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc
Requires:	ncurses-devel

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
/usr/bin/htop
/usr/share/applications/htop.desktop
/usr/share/man/man1/htop.1.gz
/usr/share/pixmaps/htop.png



%changelog

