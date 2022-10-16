import kivy
from kivy.app import App
from kivy.lang import Builder

USERS = {'test': '12345'}

kivy.require('1.9.1')

# building kv file as string
kv_file = Builder.load_file('login.kv')


class LoginApp(App):
    def check_credentials(self):
        username = self.root.ids.username.text
        password = self.root.ids.password.text
        if username in USERS.keys():
            if password == USERS[username]:
                self.root.ids.result.text = 'Logged in'

    def build(self):
        return kv_file


if __name__ == '__main__':
    kv = LoginApp()
    kv.run()
