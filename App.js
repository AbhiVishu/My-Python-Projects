import React, { Component } from "react";
import { Platform, StyleSheet, Text, View } from "react-native";

import Options from "./screens/options";
import { Provider as PaperProvider } from "react-native-paper";

class App extends Component {
  render() {
    return (
      <PaperProvider>
        <Options />
      </PaperProvider>
    );
  }
}

const styles = StyleSheet.create({

});

export default App;
