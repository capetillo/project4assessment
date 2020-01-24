import React, { Component } from "react";
import "./App.css";
import TodoList from "./TodoList";
import TodoItems from "./TodoItems";
class App extends Component {
  constructor() {
    super();
    this.state = {
      checkmark: "X",
      items: [],
      currentItem: { text: "", key: "" }
    };
  }

  updateItem = () => {
    this.setState({ checkmark: "✔" });
  };
  // onClickButton2 = () => {
  //   this.setState({
  //     text: 'clicked 2'
  //   });
  // }

  deleteItem = key => {
    const filteredItems = this.state.items.filter(item => {
      return item.key !== key;
    });
    this.setState({
      items: filteredItems
    });
  };

  handleInput = e => {
    const itemText = e.target.value;
    const currentItem = { text: itemText, key: Date.now() };
    this.setState({
      currentItem
    });
  };

  addItem = e => {
    e.preventDefault();
    const newItem = this.state.currentItem;
    if (newItem.text !== "") {
      console.log(newItem);
      const items = [...this.state.items, newItem];
      this.setState({
        items: items,
        currentItem: { text: "", key: "" }
      });
    }
  };

  render() {
    return (
      <div className="App">
        <TodoList
          addItem={this.addItem}
          inputElement={this.inputElement}
          handleInput={this.handleInput}
          currentItem={this.state.currentItem}
        />
        <TodoItems
          entries={this.state.items}
          deleteItem={this.deleteItem}
          updateItem={this.updateItem}
          checkmark={this.state.checkmark}
        />
      </div>
    );
  }
}
export default App;
