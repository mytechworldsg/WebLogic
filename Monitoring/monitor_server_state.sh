export WL_HOME=/u01/oracle/Middleware/Oracle_Home
$WL_HOME/oracle_common/common/bin/setWlstEnv.sh

$WL_HOME/oracle_common/common/bin/wlst.sh monitor_server_state.py > monitor_server_state.out

if grep -E 'SHUTDOWN|SUSPENDING|FAILED' monitor_server_state.out; then
    echo "Send Email"
else
    echo "All server are up"
fi
