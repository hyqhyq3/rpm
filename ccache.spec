Name:		ccache
Version:	3.1.9
Release:	1%{?dist}
Summary:	ccache

Group:		Development/Tools
License:	GPL
URL:		http://gnu.org
Source0:	%{name}-%{version}.tar.xz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc
Requires:	gcc

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir %{buildroot}/%{_libexecdir}/ccache/bin -p
ln -s %{_bindir}/ccache %{buildroot}/%{_libexecdir}/ccache/bin/gcc 
ln -s %{_bindir}/ccache %{buildroot}/%{_libexecdir}/ccache/bin/g++
ln -s %{_bindir}/ccache %{buildroot}/%{_libexecdir}/ccache/bin/cc 
ln -s %{_bindir}/ccache %{buildroot}/%{_libexecdir}/ccache/bin/c++


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc

%{_bindir}
%{_datadir}
%{_libexecdir}


%changelog

