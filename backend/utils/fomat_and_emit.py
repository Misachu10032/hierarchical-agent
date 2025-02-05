from flask_socketio import  emit
def format_and_emit(result,tool):

    response = str(result["messages"][-1])  # Convert to string
    message = {
        "tool": tool,
        "content": response
    }
 
    emit('detailed_data', message)
