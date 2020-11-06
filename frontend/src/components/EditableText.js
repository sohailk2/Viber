import React, { useState, useEffect } from 'react';

class EditableText extends React.Component{
    constructor(props){
      super(props)
      this.state = {
        name: props.name,
        type: props.type||'text',
        value: props.value||'',
        editClassName: props.editClassName,
        edit: false
      }
    }
    edit() {
      this.setState({edit:this.state.edit!==true})
    }
    render() {
      return (
        this.state.edit===true&&
        <input 
          name={this.state.name}
          type={this.state.type}
          value={this.state.value}
          className={this.state.editClassName}
          autoFocus
          onFocus={event=>{
            const value = event.target.value
            event.target.value = ''
            event.target.value = value
            this.setState({backup:this.state.value})
          }}
          onChange={event=>{
            this.setState({value:event.target.value})
          }}
          onBlur={event=>{
            this.setState({edit:false})
            if (this.state.value != this.props.value) {
                this.props.callback(this.state.value);
            }
          }}
          onKeyUp={event=>{
            if(event.key==='Escape') {
              this.setState({edit:false, value:this.state.backup})
            }
          }}
        />
        ||
        <span onClick={event=>{
            this.setState({edit:this.state.edit!==true})
          }}>
          {this.state.value}
        </span>
      )
    }
  }

  export default EditableText;