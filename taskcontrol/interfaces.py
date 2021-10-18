
from dataclasses import dataclass
import abc


@dataclass(frozen=True)
class ObjectModificationBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, config):
        raise NotImplementedError
    
    @abc.abstractmethod
    def fetch(self, config):
        raise NotImplementedError
    
    @abc.abstractmethod
    def update(self, config):
        raise NotImplementedError
    
    @abc.abstractmethod
    def delete(self, config):
        raise NotImplementedError


@dataclass(frozen=True)
class PicklesBase(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def __init__(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, config):
        raise NotImplementedError
    
    @abc.abstractmethod
    def insert(self, config):
        raise NotImplementedError
    
    @abc.abstractmethod
    def append(self, config):
        raise NotImplementedError
    
    @abc.abstractmethod
    def update(self, config):
        raise NotImplementedError
    
    @abc.abstractmethod
    def search(self, config):
        raise NotImplementedError
    
    @abc.abstractmethod
    def delete(self, config):
        raise NotImplementedError
    

@dataclass(frozen=True)
class AuthsBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def init_db(self, path, name):
        raise NotImplementedError

    @abc.abstractmethod
    def init_tables(self, conn):
        raise NotImplementedError

    @abc.abstractmethod
    def init_superuser(self, conn):
        raise NotImplementedError

    @abc.abstractmethod
    def create_user(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update_user(self):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_user(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self):
        raise NotImplementedError

    @abc.abstractmethod
    def change_password(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_permissions(self, options):
        # user/role, action, permissions
        raise NotImplementedError

    @abc.abstractmethod
    def update_permissions(self, options):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_permissions(self, options):
        raise NotImplementedError

    @abc.abstractmethod
    def get_permissions(self, options):
        raise NotImplementedError

    @abc.abstractmethod
    def create_role(self, options):
        # role
        raise NotImplementedError

    @abc.abstractmethod
    def update_role(self, options):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_role(self, options):
        raise NotImplementedError

    @abc.abstractmethod
    def get_role(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_permissions(self, user):
        # user, role, action, permissions
        raise NotImplementedError

    @abc.abstractmethod
    def is_authenticated(self):
        # true/false
        raise NotImplementedError


@dataclass(frozen=True)
class PubSubsBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def register_publisher(self):
        pass
    
    @abc.abstractmethod
    def register_subscriber(self):
        pass
    
    @abc.abstractmethod
    def register_event(self):
        pass
        
    @abc.abstractmethod
    def __process(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send(self, event_object):
        raise NotImplementedError
    
    @abc.abstractmethod
    def receive(self, event_object):
        raise NotImplementedError


@dataclass(frozen=True)
class SocketsBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, **kwargs):
        raise NotImplementedError
    
    @abc.abstractmethod
    def socket_create(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def socket_accept(self):
        raise NotImplementedError

    @abc.abstractmethod
    def socket_listen(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def socket_close(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send(self):
        raise NotImplementedError

    @abc.abstractmethod
    def receive(self):
        raise NotImplementedError


@dataclass(frozen=True)
class HooksBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def hook_state(self):
        raise NotImplementedError

    @abc.abstractmethod
    def service_run(self):
        raise NotImplementedError

    @abc.abstractmethod
    def service_stop(self):
        raise NotImplementedError

    @abc.abstractmethod
    def register_hook(self):
        raise NotImplementedError

    @abc.abstractmethod
    def register_receiver(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send(self):
        raise NotImplementedError

    @abc.abstractmethod
    def receive(self):
        raise NotImplementedError


@dataclass(frozen=True)
class SQLBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, conn, options):
        raise NotImplementedError

    @abc.abstractmethod
    def find(self, conn, options):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, conn, options):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, conn, options):
        raise NotImplementedError

    @abc.abstractmethod
    def db_create(self, conn, options):
        pass

    @abc.abstractmethod
    def db_alter(self, conn, options):
        pass

    @abc.abstractmethod
    def db_delete(self, conn, options):
        pass

    @abc.abstractmethod
    def db_find(self, conn, options):
        pass

    @abc.abstractmethod
    def table_create(self, conn, options):
        pass

    @abc.abstractmethod
    def table_alter(self, conn, options):
        pass

    @abc.abstractmethod
    def table_delete(self, conn, options):
        pass

    @abc.abstractmethod
    def table_find(self, conn, options):
        pass


@dataclass(frozen=True)
class LogsBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, config):
        raise NotImplementedError

    @abc.abstractmethod
    def log(self, logger_options):
        raise NotImplementedError


@dataclass(frozen=True)
class PluginsBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def plugin_create(self, name, task_instance):
        raise NotImplementedError


@dataclass(frozen=True)
class TimeBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def time(self, name, task_instance):
        raise NotImplementedError


@dataclass(frozen=True)
class CommandsBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, config):
        raise NotImplementedError

    @abc.abstractmethod
    def execute(self, config):
        raise NotImplementedError

    @abc.abstractmethod
    def close(self, config):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, config):
        raise NotImplementedError


@dataclass(frozen=True)
class SshBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, options):
        raise NotImplementedError

    @abc.abstractmethod
    def connect(self, options):
        raise NotImplementedError

    @abc.abstractmethod
    def execute(self, options):
        raise NotImplementedError

    @abc.abstractmethod
    def close(self, options):
        raise NotImplementedError

