import React, { Component } from "react";
import { Platform, StyleSheet, View, ScrollView } from "react-native";

import {
  Button,
  Chip,
  Modal,
  Portal,
  Text,
  Card,
  Provider
} from "react-native-paper";
import ImagePicker from "react-native-image-picker";
import RNTesseractOcr from "react-native-tesseract-ocr";

const options = {
  title: "Select a Photo",
  takePhotoButtonTitle: "Take a Photo",
  chooseFromLibraryButtonTitle: "Choose from gallary",
  quality: 1
};

const tessOptions = {
  whitelist: null,
  blacklist: "1234567890'!\"#$%&/()={}[]+*-_:;<>"
};

class Options extends Component {
  state = {
    avatarSource: "",
    ocr: "",
    isLoading: false,
    showContent: false,
    visible: false
  };
  _hideModal = () => this.setState({ visible: false });

  selectPhoto = () => {
    ImagePicker.showImagePicker(options, response => {
      console.log("Response = ", response);

      if (response.didCancel) {
        console.log("User cancelled image picker");
      } else if (response.error) {
        console.log("ImagePicker Error: ", response.error);
      } else if (response.customButton) {
        console.log("User tapped custom button: ", response.customButton);
      } else {
        // const source = { uri: response.uri };

        // You can also display the image using data:
        // const source = { uri: 'data:image/jpeg;base64,' + response.data };

        this.setState({
          avatarSource: response.path
        });
        this.ocrFunc();
      }
    });

    console.log(this.state.avatarSource);
  };

  ocrFunc = () => {
    this.setState({ isLoading: true });
    RNTesseractOcr.recognize(
      this.state.avatarSource,
      "LANG_ENGLISH",
      tessOptions
    )
      .then(result => {
        this.setState({ ocrResult: result, showContent: true, visible: true });
        console.log("OCR Result: ", result);
        this.setState({ ocr: result });
      })
      .catch(err => {
        this.setState({ isLoading: false });
        console.log("OCR Error: ", err);
      })
      .done();
  };

  render() {
    if (this.state.isLoading === false) {
      return (
        <Portal style={{ justifyContent: "center", alignItems: "center" }}>
          <Chip avatar="../assets/files.png" onPress={this.selectPhoto}>
            Select Photo
          </Chip>
        </Portal>
      );
    } else if (this.state.isLoading === true) {
      return (
        <Button icon="loading" mode="text" loading={true} disabled={true}>
          Do something while we are recognising text...
        </Button>
      );
    } else if (this.state.showContent) {
      return (
        <Provider>
          <Portal>
            <Modal visible={visible} onDismiss={this._hideModal}>

            </Modal>
          </Portal>
        </Provider>
      );
    }
  }
}

const styles = StyleSheet.create({});

export default Options;

// <Card
// style={{
//   borderRadius: 20,
//   marginLeft: 20,
//   marginRight: 20,
//   marginBottom: 20
// }}
// elevation={10}
// >
// <Card.Title
//   title="Recognised Text"
//   subtitle="This may not be perfect..."
//   left={props => <Avatar.Icon {...props} icon="folder" />}
// />
// <Card.Content>
//   <ScrollView>{/* <Text>{this.state.ocr}</Text> */}</ScrollView>
// </Card.Content>
// <Card.Actions>
//   <Button>Cancel</Button>
//   <Button>Ok</Button>
// </Card.Actions>
// </Card>
