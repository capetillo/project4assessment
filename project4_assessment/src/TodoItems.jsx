import React, { Component } from "react";
import "./TodoItems.css";

class TodoItems extends Component {
  createTasks = item => {
    return (
      <div>
        <li
          key={item.key}
          style={{ display: "flex" }}
          onClick={() => this.props.updateItem(item.key)}
        >
          <img
            src="https://www.pngkey.com/png/full/204-2045715_muscle-man-fit-men.png"
            alt="hunk"
            onClick={() => this.props.deleteItem(item.key)}
            style={{ height: "50%", width: "50%", marginRight: "2rem" }}
          />
          <span> {item.text}</span>
        </li>
        <button onClick={this.props.updateItem}>{this.props.checkmark}</button>
      </div>
    );
  };
  render() {
    const todoEntries = this.props.entries;
    const listItems = todoEntries.map(this.createTasks);
    return <ul className="theList">{listItems}</ul>;
  }
}
export default TodoItems;
