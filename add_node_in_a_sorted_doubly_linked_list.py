def sortedllist(llist.head,data):
  if llist.head==None:
    return
  else:
    current=llist.head
    while current.next!=None:
      if data>current.data:
        current=current.next
      else:
        break
    new_node=DoublyLinkedListNode(data)
    if data>current.data:
      new_node.prev=current
      current.next=new_node
    elif data<llist.data:
      new_node.next=llist
      llist.prev=new_node
      llist=new_node
    else:
      new_node..next=current
      new_node.prev=current.prev
      current.prev.next=new_node
      current.prev=new_node
  return llist.head 
      
            
            
