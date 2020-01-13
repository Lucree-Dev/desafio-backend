PIPE_DIR=/tmp/lucree.setup.lock

close(){
  rm $PIPE_DIR
  exit 1
}

error(){
  #If there's no args
  if [ -z "$1" ]
  then
    return
  fi

  #Show a custom output
  echo -e "$(tput bold)$(tput setaf 1)- ERROR: $1 $(tput sgr0)"
  #Remove FIFO from tmp
  exit
}

goget(){
  # If there's no args
  if [ -z "$1" ]
  then
    error "Missing go package"
  fi

  #Running process getting in concurrency
  ( 
    #Send to FIFO response 
    ( `go get -u $1` && echo yes || echo no ) > $PIPE_DIR
  ) &

  #Save cursor position
  tput sc
  echo -e "$(tput setaf 3)Installing $2 (https://$1)$(tput sgr0)"

  n=0
  arr=( "\U25F4" "\U25F5" "\U25F6" "\U25F7")

  while true; do
    if [ ! -e $PIPE_DIR ]
    then
      error "Another setup is running"
      break 
    fi

    #Here read waiting (no_blocking) 100ms
    read -t 0.1 -r line < $PIPE_DIR
    #If there's a response from FIFO
    if [ ! -z "$line" ]
    then
      case $line in
      "no") error "Install $1";;  #Response is Error
      "yes") break;;               #Response is OK
      esac
    fi

    #Below show a simple loading
    echo -ne "\r$(tput setaf 4) $(tput bold) ${arr[n]} Installing$(tput sgr0)"
    n=$(((n+1) % 4))

    if [[ $n -eq 5 ]]
    then
      n=0
    fi
  done
  
  tput rc
  tput ed

  #! `go get -u $1` && error "Install $1"
  echo -e "$(tput setaf 2)+ $2 Installed"
}

setup() {
  if [ -e $PIPE_DIR ]
  then
    echo "$(tput setaf 3) Case last script had interrupted, use rm $PIPE_DIR $(tput sgr0)"
    error "Another setup script is running, it was interrupted"
  fi

  #Create a fifo to communication between the processes
  mkfifo $PIPE_DIR

  echo "Author: Paulo Rodrigues Camacan"
  echo "Install all necessary components to run"

  echo "Installing Go packages"
  goget "github.com/go-chi/chi" "GoChi"
  goget "github.com/go-chi/auth/jwt" "GoChi-JWT"
  goget "github.com/dgrijalva/jwt-go" "GO-JWT"
  goget "github.com/go-chi/render" "GoChi-Render"
  goget "go.mongodb.org/mongo-driver/mongo" "GoMongoDrive"
  echo "$(tput bold)$(tput setaf 2)ALL PACKAGES INSTALLED!$(tput sgr0)"
  close
}

#Call setup method
setup