import requests
import json

class Callback(object):

    def __init__(self):
        self.validation_data = None

    def set_params(self, params):
        self.params = params

    def set_model(self, model):
        self.model = model

    def on_epoch_begin(self, epoch, logs=None):
        pass

    def on_epoch_end(self, epoch, logs=None):
        pass

    def on_batch_begin(self, batch, logs=None):
        pass

    def on_batch_end(self, batch, logs=None):
        pass

    def on_train_begin(self, logs=None):
        pass

    def on_train_end(self, logs=None):
        pass

class CodeMonitor():

    def __init__(self, conv_id):
        self.conv_id = conv_id
        self.send_message("All ready!")

    def send_message(self, message):
        requests.post("https://code-monitor.herokuapp.com/sendMessage",
                      data=json.dumps({"text":message,"id":self.conv_id}),
                      headers={'Content-type': 'application/json', 'Accept': 'text/plain'})

class FitMonitor(Callback):

    def __init__(self, conv_id):
        super(FitMonitorCallback, self).__init__()
        self.code_monitor = CodeMonitor(conv_id)

    def on_train_begin(self, logs=None):
        self.epochs = self.params['epochs']
        self.code_monitor.send_message("the training started")

    def on_epoch_end(self, epoch, logs=None):
        self.code_monitor.send_message(self.__format_message(epoch, logs))

    def on_train_end(self, logs=None):
        self.code_monitor.send_message("the training is over")

    def __format_message(self, epoch, logs, l=6):
        append_message = "\n\n"

        message = "Epoch " + str(epoch + 1) + " of " + str(self.epochs)

        if "val_loss" in logs:
            append_message += "val_loss = " + str(logs["val_loss"])[:l] + "\n"

        if "val_acc" in logs:
            append_message += "val_acc = " + str(logs["val_acc"])[:l] + "\n"

        if "loss" in logs:
            append_message += "loss = " + str(logs["loss"])[:l] + "\n"

        if "acc" in logs:
            append_message += "acc = " + str(logs["acc"])[:l] + "\n"

        if(len(append_message) > 2):
            message += append_message

        return message
