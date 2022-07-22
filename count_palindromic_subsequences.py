def countPs(s):
   # Code here
    MOD=1000000007
    N=len(s)
    dp=[[0 for i in range(N)]for j in range(N)]
    for g in range(N):
        i,j=0,g
        while j<N:
            if g==0:
                dp[i][j]=1
                i+=1
                j+=1
            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=3
                    i+=1
                    j+=1
                    
                else:
                    dp[i][j]=2
                    i+=1
                    j+=1
            else:
                if s[i]==s[j]:
                    dp[i][j]=(dp[i][j-1]+dp[i+1][j]+1)%MOD
                    i+=1
                    j+=1
                else:
                    dp[i][j]=(dp[i][j-1]+dp[i+1][j]-dp[i+1][j-1])%MOD
                    i+=1
                    j+=1
    return dp[0][N-1]


# string="abcd"
string="mbcgepnkdqemhmkuqosgeonbcrphobcmbhrgppkfpdqckigsomktpsurknsospighufulqijcupisnuqcqfpuckrndmqeeklqfcrfnemeghmnlunlpslncqllmbebnoudihgpigrfbrqbcurmqnfroheqltkbnpocousjepehgppmblodppsqrglprtekmsqlqekhjseotocgkfcrkssmmenhitupdcoujscnetbrrcdoctqdfssupfnuolrobckseuromqsuoctmnbudnthrctndtrnietrkqbropugptpuhclftohuendhhnpnhqqkmksigbcrtrtjtmhonnumnnupgtntdhefushmrshselrdfqnoddmqqhjrjtknmokrlgdrcomnbjdlcothrhgsljreflusnnnrkckstoluhduguicfomgjkorgmujoonekscbikeshbqfqfrbcmspqphujltqebostmbkunhhhqmdqdqmfsbekeonmsiqsbomhmrtnqtmutrbmrlthhieihqjebklckemustsufbqmbjcqdtkdjscmdsrkkqdfojplektrsinjfbhmfoumqirfehdhgdkejefupstmhqesqobcqftpgbrckqrjqdosfjschbhbuobhriguipdkeeggbtecsqheelrqiqfdokqhrdsdcifnkulloeckeghochpdfjpqesqmqsngcbpngjurdsbhtsilkoiglbgmofnjuojtgjqnpgobmfehjnqbfmternugrhbnrgqusloiuusqogtqsclesqsmhjghqdtqkgikghflotgfmkdngklcorqlegpdidptohlgnnnflhtcmpcehogooflhujpichtknfqicpkjmgjjdnmtsprcueeolruiqjpeldelnukfitfgqsdejupshdtebtqfrqbtuttkldbuupidurhimnrmpdfjtbuinfchjormhissgpdbisugtrqqdiqekpnicpej"
print(countPs(string))
