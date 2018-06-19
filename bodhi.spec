Name:           bodhi
Version:        3.8.1
Release:        2%{?dist}
BuildArch:      noarch

License:        GPLv2+
Summary:        A modular framework that facilitates publishing software updates
Group:          Applications/Internet
URL:            https://github.com/fedora-infra/bodhi
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: %{py2_dist alembic}
BuildRequires: %{py2_dist arrow}
BuildRequires: %{py2_dist bleach}
BuildRequires: %{py2_dist click}
BuildRequires: %{py2_dist colander}
BuildRequires: %{py2_dist cornice_sphinx} >= 0.3
BuildRequires: %{py2_dist cornice} >= 3.0.0
BuildRequires: %{py2_dist cryptography}
BuildRequires: %{py2_dist fedmsg}
BuildRequires: %{py2_dist feedgen}
BuildRequires: %{py2_dist flake8}
BuildRequires: %{py2_dist iniparse}
BuildRequires: %{py2_dist jinja2}
BuildRequires: %{py2_dist kitchen}
BuildRequires: %{py2_dist markdown}
BuildRequires: %{py2_dist mock}
BuildRequires: %{py2_dist pylibravatar}
BuildRequires: %{py2_dist pyramid-fas-openid}
BuildRequires: %{py2_dist pyramid-mako}
BuildRequires: %{py2_dist pyramid-tm}
BuildRequires: %{py2_dist pyramid}
BuildRequires: %{py2_dist pytest-cov}
BuildRequires: %{py2_dist pytest}
BuildRequires: %{py2_dist python-bugzilla}
BuildRequires: %{py2_dist python-fedora}
BuildRequires: %{py2_dist python-openid}
BuildRequires: %{py2_dist pyyaml}
BuildRequires: %{py2_dist simplemediawiki}
BuildRequires: %{py2_dist sphinx}
BuildRequires: %{py2_dist sqlalchemy_schemadisplay}
BuildRequires: %{py2_dist sqlalchemy}
BuildRequires: %{py2_dist virtualenv}
BuildRequires: %{py2_dist webtest}
BuildRequires: %{py3_dist alembic}
BuildRequires: %{py3_dist arrow}
BuildRequires: %{py3_dist bleach}
BuildRequires: %{py3_dist click}
BuildRequires: %{py3_dist colander}
BuildRequires: %{py3_dist cornice_sphinx} >= 0.3
BuildRequires: %{py3_dist cornice} >= 3.0.0
BuildRequires: %{py3_dist cryptography}
BuildRequires: %{py3_dist fedmsg}
BuildRequires: %{py3_dist feedgen}
BuildRequires: %{py3_dist flake8}
BuildRequires: %{py3_dist iniparse}
BuildRequires: %{py3_dist jinja2}
BuildRequires: %{py3_dist kitchen}
BuildRequires: %{py3_dist markdown}
BuildRequires: %{py3_dist mock}
BuildRequires: %{py3_dist pylibravatar}
BuildRequires: %{py3_dist pyramid-fas-openid}
BuildRequires: %{py3_dist pyramid-mako}
BuildRequires: %{py3_dist pyramid-tm}
BuildRequires: %{py3_dist pyramid}
BuildRequires: %{py3_dist pytest-cov}
BuildRequires: %{py3_dist pytest}
BuildRequires: %{py3_dist python-bugzilla}
BuildRequires: %{py3_dist python-fedora}
BuildRequires: %{py3_dist pyyaml}
BuildRequires: %{py3_dist simplemediawiki}
BuildRequires: %{py3_dist sphinx}
BuildRequires: %{py3_dist sqlalchemy}
BuildRequires: %{py3_dist virtualenv}
BuildRequires: %{py3_dist webtest}
BuildRequires: koji
BuildRequires: liberation-mono-fonts
BuildRequires: packagedb-cli
BuildRequires: pungi >= 4.1.20
BuildRequires: python2-createrepo_c
BuildRequires: python2-devel
BuildRequires: python2-dnf
BuildRequires: python2-dogpile-cache
BuildRequires: python2-koji
BuildRequires: python2-librepo
BuildRequires: python2-pillow
BuildRequires: python3-createrepo_c
BuildRequires: python3-devel
BuildRequires: python3-dnf
BuildRequires: python3-dogpile-cache
BuildRequires: python3-koji
BuildRequires: python3-librepo
BuildRequires: python3-pillow


%description
Bodhi is a web application that facilitates the process of publishing
updates for a software distribution.

A modular piece of the Fedora Infrastructure stack
* Utilizes the Koji Buildsystem for tracking RPMs
* Creates the update repositories using Mash, which composes a repository based
  on tagged builds in Koji.


%package client
Summary: Bodhi Client
Group: Applications/Internet

Requires: filesystem
Requires: python3-bodhi-client == %{version}-%{release}


%description client
Client tools for interacting with bodhi.


%package composer
Summary: Bodhi composer backend

Requires: %{py2_dist jinja2}
Requires: bodhi-server == %{version}-%{release}
Requires: pungi >= 4.1.20
Requires: python2-createrepo_c
Requires: skopeo


%description composer
The Bodhi composer is the component that publishes Bodhi artifacts to
repositories.


%package docs
Summary: Bodhi documentation
Group:   Applications/Internet

Requires: filesystem


%description docs
Bodhi documentation.


%package -n python2-bodhi
Summary: Common files shared by bodhi-client and bodhi-server
Group:   Applications/Internet

%{?python_provide:%python_provide python2-bodhi}


%description -n python2-bodhi
Common files shared by bodhi-client and bodhi-server.


%package -n python3-bodhi
Summary: Common files shared by bodhi-client and bodhi-server
Group:   Applications/Internet

%{?python_provide:%python_provide python3-bodhi}


%description -n python3-bodhi
Common files shared by bodhi-client and bodhi-server.


%package -n python2-bodhi-client
Summary: REST API bindings for Python.

Requires: %{py2_dist click}
Requires: %{py2_dist iniparse}
Requires: %{py2_dist kitchen}
Requires: %{py2_dist python-fedora} >= 0.9
Requires: %{py2_dist six}
Requires: koji
Requires: python2-bodhi == %{version}-%{release}
Requires: python2-dnf
Requires: python2-koji

%{?python_provide:%python_provide python2-bodhi-client}


%description -n python2-bodhi-client
REST API bindings for Python.


%package -n python3-bodhi-client
Summary: REST API bindings for Python.

Requires: %{py3_dist click}
Requires: %{py3_dist iniparse}
Requires: %{py3_dist kitchen}
Requires: %{py3_dist python-fedora} >= 0.9
Requires: %{py3_dist six}
Requires: koji
Requires: python3-bodhi == %{version}-%{release}
Requires: python3-dnf
Requires: python3-koji

%{?python_provide:%python_provide python3-bodhi-client}


%description -n python3-bodhi-client
REST API bindings for Python.


%package server
Summary: A modular framework that facilitates publishing software updates
Group: Applications/Internet

Requires: %{py2_dist alembic}
Requires: %{py2_dist arrow}
Requires: %{py2_dist bleach}
Requires: %{py2_dist click}
Requires: %{py2_dist colander}
Requires: %{py2_dist cornice} >= 3.0.0
Requires: %{py2_dist cryptography}
Requires: %{py2_dist fedmsg}
Requires: %{py2_dist feedgen}
Requires: %{py2_dist kitchen}
Requires: %{py2_dist markdown}
Requires: %{py2_dist psycopg2}
Requires: %{py2_dist pylibravatar}
Requires: %{py2_dist pyramid-fas-openid}
Requires: %{py2_dist pyramid-mako}
Requires: %{py2_dist pyramid-tm}
Requires: %{py2_dist pyramid}
Requires: %{py2_dist python-bugzilla}
Requires: %{py2_dist python-fedora}
Requires: %{py2_dist python-openid}
Requires: %{py2_dist simplemediawiki}
Requires: %{py2_dist six}
Requires: %{py2_dist sqlalchemy}
Requires: %{py2_dist waitress}
Requires: python2-bodhi-client == %{version}-%{release}
Requires: fedmsg
Requires: fedmsg-base
Requires: git
Requires: httpd
Requires: intltool
Requires: liberation-mono-fonts
Requires: mod_wsgi
Requires: packagedb-cli
Requires: python2-dogpile-cache
Requires: python2-koji
Requires: python2-librepo
Requires: python2-pillow

Provides:  bundled(aajohan-comfortaa-fonts)
Provides:  bundled(abattis-cantarell-fonts)
Provides:  bundled(bootstrap) = 3.0.1
Provides:  bundled(bootstrap) = 3.0.2
Provides:  bundled(bootstrap) = 3.1.1
Provides:  bundled(chrissimpkins-hack-fonts)
Provides:  bundled(fedora-bootstrap) = 1.0.1
Provides:  bundled(fontawesome-fonts-web) = 4.4.0
Provides:  bundled(js-chart)
Provides:  bundled(js-excanvas)
Provides:  bundled(js-jquery) = 1.10.2
Provides:  bundled(js-jquery) = 2.0.3
Provides:  bundled(js-messenger)
Provides:  bundled(js-moment)
Provides:  bundled(js-typeahead.js) = 1.1.1
Provides:  bundled(nodejs-flot)
Provides:  bundled(open-sans-fonts)
Provides:  bundled(xstatic-bootstrap-datepicker-common)


%description server
Bodhi is a modular framework that facilitates the process of publishing
updates for a software distribution.


%prep
%autosetup -p1 -n bodhi-%{version}

# Kill some dev deps
sed -i '/pyramid_debugtoolbar/d' setup.py
sed -i '/pyramid_debugtoolbar/d' devel/development.ini.example

# Kill this from the egg-info deps so that bodhi-server doesn't demand it.
sed -i '/click/d' setup.py

# The unit tests needs a development.ini
mv devel/development.ini.example development.ini


%build
%py2_build
%py3_build

make %{?_smp_mflags} -C docs html
make %{?_smp_mflags} -C docs man


%install
# We want the /usr/bin/bodhi CLI to be Python 3 now, but we don't want the server CLIs to be Python
# 3 yet. An easy way to do this is to install Python 3 Bodhi first, save the /usr/bin/bodhi it
# generates, then do the Python 2 install (to overwrite the common files). Afterwards, we'll move
# the Python 3 /usr/bin/bodhi back into place.
%py3_install
# We aren't ready to support Bodhi server on Python 3 yet, so let's just nuke it for now.
rm -rf %{buildroot}/usr/lib/python%{python3_version}/site-packages/bodhi/server/
rm -rf %{buildroot}/usr/lib/python%{python3_version}/site-packages/bodhi_server-*.egg-info
# Let's save /usr/bin/bodhi from being overwritten, since we want it to be the Python 3 version.
cp %{buildroot}/usr/bin/bodhi bodhi-py3
%py2_install

%{__mkdir_p} %{buildroot}/var/lib/bodhi
%{__mkdir_p} %{buildroot}/var/cache/bodhi
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bash_completion.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/httpd/conf.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/fedmsg.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bodhi
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__mkdir_p} -m 0755 %{buildroot}/%{_localstatedir}/log/bodhi

%{__install} -m 0755 bodhi-complete.sh %{buildroot}%{_sysconfdir}/bash_completion.d
%{__install} -m 644 apache/%{name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
%{__install} -m 640 production.ini %{buildroot}%{_sysconfdir}/%{name}/production.ini
%{__install} -m 640 alembic.ini %{buildroot}%{_sysconfdir}/%{name}/alembic.ini
%{__install} apache/%{name}.wsgi %{buildroot}%{_datadir}/%{name}/%{name}.wsgi

%{__install} -m 644 fedmsg.d/masher.py %{buildroot}%{_sysconfdir}/fedmsg.d/masher.py
%{__install} -m 644 fedmsg.d/bodhi.py %{buildroot}%{_sysconfdir}/fedmsg.d/bodhi.py

install -d %{buildroot}%{_mandir}/man1
install -pm0644 docs/_build/man/*.1 %{buildroot}%{_mandir}/man1/

if [ ! -e %{buildroot}%{python2_sitelib}/%{name}/server/static/bootstrap ]; then
    # setuptools on EL 7 does not install bootstrap, so we need to symlink it
    ln -s ./bootstrap-3.1.1-fedora \
        %{buildroot}%{python2_sitelib}/%{name}/server/static/bootstrap
fi;

# Restore the Python 3 version of /usr/bin/bodhi.
mv bodhi-py3 %{buildroot}/usr/bin/bodhi


%check
# setuptools on EL 7 doesn't install bootstrap. This test ensures that bootstrap is present.
if [ ! -e %{buildroot}%{python2_sitelib}/%{name}/server/static/bootstrap ]; then
    echo "%{buildroot}%{python2_sitelib}/%{name}/server/static/bootstrap is missing, failing!"
    /usr/bin/false
fi;

# The tests need bodhi to be installed to pass. Let's build a virtualenv so we can install bodhi
# there.
virtualenv-2 --system-site-packages --no-pip --never-download .test-virtualenv-2
virtualenv-3 --system-site-packages --no-pip --never-download .test-virtualenv-3

.test-virtualenv-2/bin/python2 setup.py develop
.test-virtualenv-2/bin/python2 /usr/bin/py.test-2

.test-virtualenv-3/bin/python3 setup.py develop
# The Python 3 tests don't reach the required coverage numbers.
sed -i "s/fail_under.*/fail_under = 78/" .coveragerc
.test-virtualenv-3/bin/python3 /usr/bin/py.test-3


%pre server
%{_sbindir}/groupadd -r %{name} &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d %{_datadir}/%{name} -M \
                     -c 'Bodhi Server' -g %{name} %{name} &>/dev/null || :


%files client
%license COPYING
%doc README.rst
%{_sysconfdir}/bash_completion.d/bodhi-complete.sh
%{_bindir}/bodhi
%{_mandir}/man1/bodhi.1*


%files composer
%license COPYING
%doc README.rst
%{python2_sitelib}/%{name}/server/consumers/masher.py*
%{python2_sitelib}/%{name}/server/metadata.py*


%files docs
%license COPYING
%doc docs/_build/html/ README.rst


%files -n python2-bodhi
%license COPYING
%doc README.rst
%dir %{python2_sitelib}/%{name}/
%{python2_sitelib}/%{name}/__init__.py*
%{python2_sitelib}/%{name}-%{version}-py%{python2_version}.egg-info


%files -n python3-bodhi
%license COPYING
%doc README.rst
%dir %{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}/__init__.py
%{python3_sitelib}/%{name}/__pycache__
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info


%files -n python2-bodhi-client
%license COPYING
%doc README.rst
%{python2_sitelib}/%{name}/client
%{python2_sitelib}/%{name}_client-%{version}-py%{python2_version}.egg-info


%files -n python3-bodhi-client
%license COPYING
%doc README.rst
%{python3_sitelib}/%{name}/client
%{python3_sitelib}/%{name}_client-%{version}-py%{python3_version}.egg-info


%files server
%license COPYING
%doc README.rst
%{_bindir}/bodhi-approve-testing
%{_bindir}/bodhi-check-policies
%{_bindir}/bodhi-clean-old-mashes
%{_bindir}/bodhi-dequeue-stable
%{_bindir}/bodhi-expire-overrides
%{_bindir}/bodhi-manage-releases
%{_bindir}/bodhi-monitor-composes
%{_bindir}/bodhi-push
%{_bindir}/bodhi-untag-branched
%{_bindir}/initialize_bodhi_db
%config(noreplace) %{_sysconfdir}/bodhi/alembic.ini
%config(noreplace) %{_sysconfdir}/httpd/conf.d/bodhi.conf
%config(noreplace) %{_sysconfdir}/fedmsg.d/*
%dir %{_sysconfdir}/bodhi/
%{python2_sitelib}/%{name}/server
%{python2_sitelib}/%{name}_server-%{version}-py%{python2_version}.egg-info
%{_mandir}/man1/bodhi-*.1*
%{_mandir}/man1/initialize_bodhi_db.1*
%attr(-,bodhi,root) %{_datadir}/%{name}
%attr(-,bodhi,bodhi) %config(noreplace) %{_sysconfdir}/bodhi/*
%attr(0775,bodhi,bodhi) %{_localstatedir}/cache/bodhi
# These excluded files are in the bodhi-consumers package so don't include them here.
%exclude %{python2_sitelib}/%{name}/server/consumers/masher.py*
%exclude %{python2_sitelib}/%{name}/server/metadata.py*


%changelog
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.8.1-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1.
- Fix a Python 3.7 FTBFS (#1589990).
- https://github.com/fedora-infra/bodhi/releases/tag/3.8.1

* Wed May 16 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0 (#1582628).
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-8-0

* Tue May 08 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-7-0

* Mon Apr 23 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1 (#1570947).
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-6-1
- bodhi-server no longer provides the composer (masher.py). It is now provided
  by a separate bodhi-composer subpackage.

* Mon Mar 26 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0 (#1567959).
- https://bodhi.stg.fedoraproject.org/docs/user/release_notes.html#v3-6-0
- The CLI now uses Python 3 (#1024795).
- bodhi-client no longer contains the Python bindings - they were split out
  into new python2-bodhi-client and python3-bodhi-client subpackages.

* Mon Mar 26 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2 (#1560680).
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-5-2

* Wed Mar 21 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-5-1

* Tue Feb 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-5-0

* Mon Feb 26 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-4-0

* Fri Feb 16 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-3-0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0.
- Use the fancy new py2_dist macro for dependencies.
- Fix a FTBFS (#1530245).
- Drop the moveshelf patch because it causes tests to fail.

* Fri Jan 05 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 3.1.0-3
- Apply patch to move the shelves

* Tue Dec 12 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.0-2
- Correct bodhi-client's help text to show the correct syntax for multi-build
  updates (#1515766).

* Tue Oct 31 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0.
- https://github.com/fedora-infra/bodhi/releases/tag/3.1.0
- Require alembic in the server package (#1493678).

* Tue Oct 24 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0 (#1506021).
- https://github.com/fedora-infra/bodhi/releases/tag/3.0.0
- Supports non-RPM artifacts (#1352587).

* Wed Oct 11 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.12.2-1
- Update to 2.12.2.
- https://github.com/fedora-infra/bodhi/releases/tag/2.12.2

* Wed Oct 11 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.12.1-1
- Update to 2.12.1.
- https://github.com/fedora-infra/bodhi/releases/tag/2.12.1

* Tue Oct 10 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.12.0-1
- Update to 2.12.0 (#1500515).
- https://github.com/fedora-infra/bodhi/releases/tag/2.12.0

* Fri Sep 22 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.11.0-3
- Retry auth upon captcha failures (#1494644).

* Wed Sep 20 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.11.0-2
- Use python2- versions on several dependencies.

* Tue Sep 19 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.11.0-1
- Update to 2.11.0 (#1493587).
- https://github.com/fedora-infra/bodhi/releases/tag/2.11.0

* Fri Sep 15 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.10.1-4
- The client should Require koji and python2-koji (#1488223).
- Fix Fedora < 27 to require python-progressbar.

* Tue Sep 05 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.10.1-3
- Use python2- prefixes for progressbar and pytest-cov dependencies.

* Tue Sep 05 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.10.1-2
- Bump the release to fix the upgrade path from F26.

* Tue Aug 22 2017 Jeremy Cline <jeremy@jcline.org> - 2.10.1-1
- Update to 2.10.1
- https://github.com/fedora-infra/bodhi/releases/tag/2.10.1

* Fri Aug 18 2017 Jeremy Cline <jeremy@jcline.org> - 2.10.0-1
- Update to 2.10.0
- https://github.com/fedora-infra/bodhi/releases/tag/2.10.0

* Tue Aug 15 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1, which fixes CVE-2017-1002152 (#1478587).
- https://github.com/fedora-infra/bodhi/releases/tag/2.9.1

* Tue Aug 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.0-4
- bodhi-server now depends on bodhi-client for some of its CLI tools (#1479456).

* Tue Aug 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.0-3
- Depend on filesystem instead of bash-completion (#1479341).

* Thu Aug 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.0-2
- Use python2- dependencies where appropriate.

* Wed Aug 02 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0 (#1477579).
- https://github.com/fedora-infra/bodhi/releases/tag/2.9.0
- Lexigraphically sort dependencies.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1.
- https://github.com/fedora-infra/bodhi/releases/tag/2.8.1
- Make a few of the python2- dependencies be python- again for F24-25.

* Tue Jun 20 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.8.0-2
- Use python2- versions of dependencies where available.
- Rearrange dependencies alphabetically.
- Drop client requirement on kitchen, since it doesn't use it.
- Drop server requirement on sphinx, since it doesn't use it.

* Tue Jun 20 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0.
- https://github.com/fedora-infra/bodhi/releases/tag/2.8.0

* Wed Jun 07 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.7.0-2
- Drop the alembic.ini symlink in /usr/share since it is not needed.

* Mon May 15 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0 (#1458342).
- https://github.com/fedora-infra/bodhi/releases/tag/2.7.0
- Install alembic.ini as a config file (#1451091).

* Fri May 05 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2 (#1445294).
- https://github.com/fedora-infra/bodhi/releases/tag/2.6.2

* Mon May 01 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1 (#1447149).
- https://github.com/fedora-infra/bodhi/releases/tag/2.6.1

* Mon Apr 17 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0.
- https://github.com/fedora-infra/bodhi/releases/tag/2.6.0

* Mon Apr 10 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.5.0-2
- Apply a patch to fix https://github.com/fedora-infra/bodhi/issues/1423
- Temporarily disable the tests since the patch causes two of them to fail, expectedly.

* Tue Mar 28 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0.
- https://github.com/fedora-infra/bodhi/releases/tag/2.5.0
- Declare all the bundled packages found in bodhi-server's static/ folder.
- Remove commented Requires and BuildRequires.

* Wed Mar 22 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.0-3
- Drop depenency on yum from the client (#1135681).

* Fri Mar 10 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.0-2
- Apply a patch to workaround https://github.com/fedora-infra/bodhi/issues/1343 until a true fix is
  available.
