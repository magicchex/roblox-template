# prompt () {
# printf "$1"
# read -p "$2"
# }
tools_bool=0

while read line
do
    if [[ $line =~ "tools" ]]; then
        tools_bool=1
    fi
    if (( $tools_bool > "0" )); then
        if [[ "$line" =~ \"([^\"]*)\" ]]; then
            tool=${BASH_REMATCH[1]%@*}
            rokit trust $tool
        fi
    fi
done < "./rokit.toml"
# prompt "Done running test\n" ""
