#import sys
#
#input_corpus=format(str(sys.argv[1]))
#output_path_details=format(str(sys.argv[2]))
#input_path_details=format(str(sys.argv[3]))

input_corpus="D:/Project2_Dryrun_Corpus.txt"
output_path_details="D:/rohith1.txt"
input_path_details="D:/Project2_Dryrun_input.txt"



empty_string="empty"
newline_string="\n"

#Storing the different lines information
file=open(input_corpus)
data=[]
for value in file:
    data.append(value)


#For queries
query_details=open(input_path_details)
queries=[]
for q in query_details:
    queries.append(q)


#Storing the terms and postings separately
ids=[]
items=[]
for i in data:
    tab_split=i.split("\t")
    ids.append(tab_split[0])
    
    a=tab_split[1].split("\n")
    items.append(a[0])


#Storing the terms details
new_items=[]
for i in items:
    new_items.append(i.split(" "))
    

#Retreiving the unique terms information
terms_info=[]
for i in items:
    x=i.split(" ")
    for j in x:
        if j not in terms_info:
            terms_info.append(j)
            
            
#Getting posting values
post=[]
for term in terms_info:
    documents=[]
    for j in range(0,len(items)):
        if term in new_items[j]:
            documents.append(ids[j])
    post.append(documents)   

final_posts=post

#DaatAnd implementation
def daatandimplementation(query):
    
    daat_and_result=""
    daat_and_string="DaatAnd"
    results_string="Results: "
    query=query.strip()
    daat_and_result=daat_and_result+daat_and_string+newline_string
    daat_and_result=daat_and_result+query+newline_string
    daat_and_result=daat_and_result+results_string
    
    #Variables initialization
    count=0
    item2=0
    item3=0
    final_list=[]
    and_list=[]
    
    terms_daat=query.strip().split(" ")
    
    for i in range(len(terms_info)):
        if terms_info[i] in terms_daat:
            and_list.append(post[i])
            
    and_list.sort(key=len)
    
    #Comparisions verification
    for item1 in range(len(and_list)-1):
        next_item=and_list[item1+1]
        first_item=and_list[item1]
        
        while len(first_item)>item2 and len(next_item)>item3:
            
            if first_item[item2]<next_item[item3]:
                count=count+1
                item2=item2+1
            elif first_item[item2]==next_item[item3]:
                count=count+1
                if first_item[item2] not in final_list:
                    final_list.append(first_item[item2])
                item2=item2+1
                item3=item3+1
            else:
                count=count+1
                item3=item3+1

    #sorting the final list
    final_list.sort()
    
    for m in range(len(and_list)):
        for n in final_list:
            if n not in and_list[m]:
                final_list.remove(n)
    
    for p in final_list:
        if p not in and_list[0]:
            final_list.remove(p)
    
    return printdaatanditems(final_list,count,terms_daat,daat_and_result) 
 

#Printing of the daat and items               
def printdaatanditems(final_list,count,terms_daat,daat_and_result):
    
    #Printing the output in required format
    if len(final_list)!=0:
        for ids in final_list:
            daat_and_result=daat_and_result+ids+" "
    else:
         daat_and_result=daat_and_result+empty_string+" "
         
    return outputprintingforandor(daat_and_result,final_list,count,terms_daat)


#Get postings method and printing it into the output file
def postings(query):
    
    #Paramters initialization
    post_result=""
    result_list=[]
    terms=[]
    get_postings="GetPostings"
    postings_list_string="Postings list: "
    
    getpostingsdata=query.strip().split(" ")
    for item in getpostingsdata:
        post_result=post_result+get_postings+newline_string
        post_result.strip()
        post_result=post_result+item+newline_string
        for i in items:
            x=i.split(" ")
            for j in x:
                if j not in terms:
                    terms.append(j)
        for i in range(len(terms)):
            if terms[i]==item:
                result_list=post[i]
        post_result=post_result+postings_list_string
        for id in result_list:
            post_result=post_result+id+" "
        post_result.strip()
        post_result=post_result+newline_string
    return post_result

    
    
#DaatOr Implementation
def daatorimplementation(query):    
    
    daat_or_result=""
    results_string="Results: "
    daat_or_string="DaatOr"
    query=query.strip()
    daat_or_result=daat_or_result+daat_or_string+newline_string
    daat_or_result=daat_or_result+query+newline_string
    daat_or_result=daat_or_result+results_string
    
    ##Paramaters initialization
    item2=0
    item3=0
    count=0   
    or_index=0
    final_list=[]
    or_list=[]
        
    terms_or=query.strip().split(" ")
    
    for i in range(len(terms_info)):
        if terms_info[i] in terms_or:
            or_list.append(final_posts[i])
            or_index+=1
    
    or_list.sort(key=len)
    final_list=or_list[0]
    
#    Comparisions verification
    for item1 in range(len(or_list)-1):
        
        next_item=or_list[item1+1]
        first_item=or_list[item1]
        
        while len(first_item)>item2 and len(next_item)>item3:
            if first_item[item2]<next_item[item3]:
                count=count+1
                item2=item2+1
            elif first_item[item2]==next_item[item3]:
                count=count+1
                item2=item2+1
                item3=item3+1
            else:
                count=count+1
                item3=item3+1
                
        for i in range(len(first_item)):
            if first_item[i] not in final_list:
                final_list.extend(first_item[i])
        
        for j in range(len(next_item)):
            if next_item[j] not in final_list:
                final_list.append(next_item[j])
                
        
        count=count+len(first_item)-item3-1
        count=count+len(next_item)-item2-1
    

    final_list.sort()
    return printdaatoritems(final_list,count,terms_or,daat_or_result)
    
#Printing of the daat or items 
def printdaatoritems(final_list,count,terms_or,daat_or_result):
    
    if len(final_list)!=0:
        for ids in final_list:
            daat_or_result=daat_or_result+ids+" "
    else:
        daat_or_result=daat_or_result+empty_string
        
    return outputprintingforandor(daat_or_result,final_list,count,terms_or)


#Output printing for daat And,Or
def outputprintingforandor(daat_result_final,final_list,count,terms):
    
    #Printing the output in required format
    results="Number of documents in results: "
    length=str(len(final_list))
    compare_string="Number of comparisons: "
    daat_result=daat_result_final+"\n"+results+length+newline_string
    daat_result=daat_result+compare_string+str(count)+newline_string
    daat_result=daat_result+tf_idfimplementation(terms,final_list)+newline_string
    return daat_result
    
#TF-IDF implementation
def tf_idfimplementation(query,retreived):
    
    tf_idf_string="TF-IDF"
    results_string="Results: "
    final_result=tf_idf_string+newline_string+results_string
    
    #Paramaters initialization
    id_ranks=[]
    final_count=len(ids)
    final_list=[]
#    tf_value=0.0
#    idf_value=0.0
#    tfidf_value=0.0
    
            
    for i in retreived:
        results=new_items[ids.index(i)]
        tfidf_value=0.0
        
        for j in query:
            tf_value=0.0
            idf_value=0.0
            count=results.count(j)
            
            tf_value=count/len(results)
            
            term=0
            for k in new_items:
                if j in k:
                    term=term+1
                    
            idf_value=final_count/term
            
            #Calculating tf-idf value
            tfidf_value=tfidf_value+tf_value*idf_value
    
        id_ranks.append(tfidf_value)

    if(len(retreived)<=0):
         final_result=final_result+empty_string+" "
    else:
        id_ranks,retreived=zip(*sorted(zip(id_ranks,retreived)))
        final_list=retreived[::-1]
        for i in final_list:
            final_result=final_result+str(i)+" "
    
    final_result=final_result.strip()
    return final_result

     
# Saving the received output to a file     
final_data=""
f = open(output_path_details, "w+")


for q in queries: 
    final_data=final_data+postings(q)
    final_data=final_data+daatandimplementation(q)
    final_data=final_data+daatorimplementation(q)+newline_string
    
f.write(final_data) 
f.close()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    