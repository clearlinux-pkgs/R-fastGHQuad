#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fastGHQuad
Version  : 1.0.1
Release  : 8
URL      : https://cran.r-project.org/src/contrib/fastGHQuad_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fastGHQuad_1.0.1.tar.gz
Summary  : Fast 'Rcpp' Implementation of Gauss-Hermite Quadrature
Group    : Development/Tools
License  : MIT
Requires: R-fastGHQuad-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
utility functions for adaptive GH quadrature. See Liu, Q. and Pierce, D. A.

%package lib
Summary: lib components for the R-fastGHQuad package.
Group: Libraries

%description lib
lib components for the R-fastGHQuad package.


%prep
%setup -q -c -n fastGHQuad
cd %{_builddir}/fastGHQuad

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651849260

%install
export SOURCE_DATE_EPOCH=1651849260
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fastGHQuad
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fastGHQuad
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fastGHQuad
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fastGHQuad || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fastGHQuad/DESCRIPTION
/usr/lib64/R/library/fastGHQuad/INDEX
/usr/lib64/R/library/fastGHQuad/LICENSE
/usr/lib64/R/library/fastGHQuad/Meta/Rd.rds
/usr/lib64/R/library/fastGHQuad/Meta/features.rds
/usr/lib64/R/library/fastGHQuad/Meta/hsearch.rds
/usr/lib64/R/library/fastGHQuad/Meta/links.rds
/usr/lib64/R/library/fastGHQuad/Meta/nsInfo.rds
/usr/lib64/R/library/fastGHQuad/Meta/package.rds
/usr/lib64/R/library/fastGHQuad/NAMESPACE
/usr/lib64/R/library/fastGHQuad/R/fastGHQuad
/usr/lib64/R/library/fastGHQuad/R/fastGHQuad.rdb
/usr/lib64/R/library/fastGHQuad/R/fastGHQuad.rdx
/usr/lib64/R/library/fastGHQuad/help/AnIndex
/usr/lib64/R/library/fastGHQuad/help/aliases.rds
/usr/lib64/R/library/fastGHQuad/help/fastGHQuad.rdb
/usr/lib64/R/library/fastGHQuad/help/fastGHQuad.rdx
/usr/lib64/R/library/fastGHQuad/help/paths.rds
/usr/lib64/R/library/fastGHQuad/html/00Index.html
/usr/lib64/R/library/fastGHQuad/html/R.css
/usr/lib64/R/library/fastGHQuad/include/fastGHQuad.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fastGHQuad/libs/fastGHQuad.so
/usr/lib64/R/library/fastGHQuad/libs/fastGHQuad.so.avx2
/usr/lib64/R/library/fastGHQuad/libs/fastGHQuad.so.avx512
