%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	Piece
Summary:	Object Oriented time objects
Name:		perl-%{pdir}-%{pnam}
Version:	1.08
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module replaces the standard localtime and gmtime functions with
implementations that return objects. It does so in a backwards
compatible manner, so that using localtime/gmtime in the way
documented in perlfunc will still return what you expect.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
#%dir %{perl_sitearch}/%{pdir}/ # -- which package should be a Time/ owner?
%{perl_sitearch}/%{pdir}/*.pm
#%dir %{perl_sitearch}/auto/%{pdir} # -- which package should be a Class/ owner?
%dir %{perl_sitearch}/auto/%{pdir}/%{pnam}
%{perl_sitearch}/auto/%{pdir}/%{pnam}/%{pnam}.*
%{_mandir}/man3/*
