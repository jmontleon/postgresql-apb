%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name: 		postgresql-apb-role
Version:	1.1.1
Release:	1%{build_timestamp}%{?dist}
Summary:	Ansible Playbook for PostgreSQL APB

License:	ASL 2.0
URL:		https://github.com/ansibleplaybookbundle/RHSCL-PostgreSQL-APB
Source0:	https://github.com/ansibleplaybookbundle/RHSCL-PostgreSQL-APB/archive/%{name}-%{version}.tar.gz
BuildArch:  	noarch

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/apb/ %{buildroot}/opt/ansible/
mv playbooks %{buildroot}/opt/apb/actions
mv roles %{buildroot}/opt/ansible/roles

%files
%doc
/opt/apb/actions
/opt/ansible/roles

%changelog
* Sun Nov 19 2017 Jason Montleon <jmontleo@redhat.com> 1.1.1-1
- Rename the templates to follow convention (rhallise@redhat.com)
- Add a log gathering script to the ci job (rhallise@redhat.com)
- Pickup 3.7 framework changes (rhallise@redhat.com)
- Fix templates to work with 3.7 (rhallise@redhat.com)
- Use the ansible-service-broker setup gate script (rhallise@redhat.com)
- Add CI to postgresql (rhallise@redhat.com)
- Bug 1512430 - Remove unnecessary wait for service (jmontleo@redhat.com)
- bump release (jesusr@redhat.com)

* Tue Nov 07 2017 Jason Montleon <jmontleo@redhat.com> 1.0.13-1
-  Bug 1508278 - Use include_tasks instead of include for updated Ansible
  version. (cchase@redhat.com)

* Fri Nov 03 2017 Jason Montleon <jmontleo@redhat.com> 1.0.12-1
- Bug 1508278 - Revert to using include for now for Ansible 2.3.2
  compatibility. (cchase@redhat.com)

* Fri Nov 03 2017 Jason Montleon <jmontleo@redhat.com> 1.0.11-1
- Bug 1509018 - Added tags to show up under the right tab in the UI.
  (cchase@redhat.com)
- Bug 1508994 - Hide password with display_type: password (cchase@redhat.com)
- Bug 1508278 - Use include_tasks instead of include (cchase@redhat.com)
- Bug 1508374 - Move password field below user field (cchase@redhat.com)

* Mon Oct 16 2017 Jason Montleon <jmontleo@redhat.com> 1.0.10-1
- Make version updatable (jmontleo@redhat.com)

* Mon Oct 16 2017 Jason Montleon <jmontleo@redhat.com> 1.0.9-1
- Bug 1500661 - Add missing quotes around default version. (chris@chasenc.com)

* Fri Oct 13 2017 Jason Montleon <jmontleo@redhat.com> 1.0.8-1
- Ensure proper templating with quotes on image (dymurray@redhat.com)

* Fri Oct 13 2017 Jason Montleon <jmontleo@redhat.com> 1.0.7-1
- stop prefixing the repository with the registry and org twice
  (jmontleo@redhat.com)

* Tue Oct 10 2017 Jason Montleon <jmontleo@redhat.com> 1.0.6-1
- Update dockerfiles (david.j.zager@gmail.com)
- Bug 1500364 - Update apb.yml with all dependent images
  (david.j.zager@gmail.com)

* Thu Oct 05 2017 Jason Montleon <jmontleo@redhat.com> 1.0.5-1
- Add support to update a dev deployment to a prod deployment
  (jmontleo@redhat.com)
- Bug 1498571 - Remove image from APB (david.j.zager@gmail.com)

* Wed Oct 04 2017 Jason Montleon <jmontleo@redhat.com> 1.0.4-1
- Bug 1498185 - Move version label onto APB spec (dymurray@redhat.com)
- Fix nightly metadata (jmontleo@redhat.com)
- Update url for postgresql apb (david.j.zager@gmail.com)
- Bumped APB spec version to 1.0 (dymurray@redhat.com)
- Updated APB to include proper providerDisplayName metadata
  (dymurray@redhat.com)

* Tue Sep 19 2017 Jason Montleon <jmontleo@redhat.com> 1.0.3-1
- new package built with tito

* Mon Aug 21 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- Fix rhscl-postgresql-apb deprovision (#116) (jmontleo@redhat.com)

* Fri Aug 18 2017 Jason Montleon <jmontleo@redhat.com> 1.0.1-1
- new package built with tito

