#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	Piece
Summary:	Time::Piece - object oriented time objects
Summary(pl.UTF-8):	Time::Piece - obiekty czasu
Name:		perl-Time-Piece
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Time/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7608cd1a565060dbef1f7e2d2a14efb9
URL:		http://search.cpan.org/dist/Time-Piece/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
This module replaces the standard localtime and gmtime functions with
implementations that return objects. It does so in a backwards
compatible manner, so that using localtime/gmtime in the way
documented in perlfunc will still return what you expect.

%description -l pl.UTF-8
Ten moduł zastępuje standardowe funkcje localtime i gmtime
implementacjami zwracającymi obiekty. Czyni to w sposób wstecznie
kompatybilny, więc używanie localtime/gmtime w sposób opisany w
perlfunc nadal będzie robić to, czego się oczekuje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Time/*.pm
%dir %{perl_vendorarch}/auto/Time/Piece
%{perl_vendorarch}/auto/Time/Piece/Piece.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Time/Piece/Piece.so
%{_mandir}/man3/*
