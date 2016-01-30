# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.proxytype -t test_proxy.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.proxytype.testing.COLLECTIVE_PROXYTYPE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_proxy.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Proxy
  Given a logged-in site administrator
    and an add proxy form
   When I type 'My Proxy' into the title field
    and I submit the form
   Then a proxy with the title 'My Proxy' has been created

Scenario: As a site administrator I can view a Proxy
  Given a logged-in site administrator
    and a proxy 'My Proxy'
   When I go to the proxy view
   Then I can see the proxy title 'My Proxy'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add proxy form
  Go To  ${PLONE_URL}/++add++Proxy

a proxy 'My Proxy'
  Create content  type=Proxy  id=my-proxy  title=My Proxy


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the proxy view
  Go To  ${PLONE_URL}/my-proxy
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a proxy with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the proxy title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
