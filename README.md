  <div class="project-description">
    <h1>The Fyers API Python client - v3</h1>
    <p>
      The official Python client for communicating with the
      <a href="https://myapi.fyers.in" rel="nofollow">Fyers API</a>
    </p>
    <h2>Documentation</h2>
    <ul>
      <li>
        <a href="https://myapi.fyers.in/docsv3" rel="nofollow"
          >Python client documentation</a
        >
      </li>
    </ul>
    <h2>Requirements</h2>
    <ul>
      <li>Python v3</li>
    </ul>
    <h2>Installation</h2>
    <p>
      Install via
      <a href="https://pypi.org/project/fyers-apiv3/" rel="nofollow">pip</a>
    </p>
    <pre><code>pip install fyers-apiv3
</code></pre>
    <h2>Breaking changes - v3</h2>
    <p>
      <code>v3</code> is a <strong>breaking</strong> major release with multiple
      internal modification to improve user experience.<br />
    </p>
    <h3>New Data Socket:</h3>
    <ul>
      <li>
        Improved tick update speed, ensuring swift and efficient market data
        updates.
      </li>
      <li>
        Introducing Lite mode for targeted last traded price (LTP) change
        updates.
      </li>
      <li>
        SymbolUpdate: Real-time symbol-specific updates for instant parameter
        changes.
      </li>
      <li>DepthUpdate: Real-time market depth changes for selected symbols.</li>
      <li>
        Increased subscription capacity, accommodating tracking of 200 symbols.
      </li>
      <li>
        Strengthened error handling callbacks for seamless issue resolution.
      </li>
    </ul>
    <h3>New Order Socket:</h3>
    <ul>
      <li>Real-time updates for orders.</li>
      <li>Real-time updates for positions.</li>
      <li>Real-time updates for trades.</li>
      <li>Real-time updates for eDIS.</li>
      <li>Real-time updates for price alerts.</li>
      <li>Improved error handling callbacks.</li>
    </ul>
    <h2>Getting started wih API</h2>
    <pre
      lang="Python"
    ><span class="kn">from</span> <span class="nn">fyers_apiv3</span> <span class="kn">import</span> <span class="n">fyersModel</span>
<span class="kn">import</span> <span class="nn">webbrowser</span>

<span class="sd">"""</span>
<span class="sd">In order to get started with Fyers API we would like you to do the following things first.</span>
<span class="sd">1. Checkout our API docs :   https://myapi.fyers.in/docsv3</span>
<span class="sd">2. Create an APP using our API dashboard :   https://myapi.fyers.in/dashboard/</span>

<span class="sd">Once you have created an APP you can start using the below SDK </span>
<span class="sd">"""</span>

<span class="c1">#### Generate an authcode and then make a request to generate an accessToken (Login Flow)</span>

<span class="sd">"""</span>
<span class="sd">1. Input parameters</span>
<span class="sd">"""</span>
<span class="n">redirect_uri</span><span class="o">=</span> <span class="s2">"APP REDIRECT URI"</span>  <span class="c1">## redircet_uri you entered while creating APP.</span>
<span class="n">client_id</span> <span class="o">=</span> <span class="s2">"XCXXXXXxxM-100"</span>                       <span class="c1">## Client_id here refers to APP_ID of the created app</span>
<span class="n">secret_key</span> <span class="o">=</span> <span class="s2">"MH*****TJ5"</span>                          <span class="c1">## app_secret key which you got after creating the app </span>
<span class="n">grant_type</span> <span class="o">=</span> <span class="s2">"authorization_code"</span>                  <span class="c1">## The grant_type always has to be "authorization_code"</span>
<span class="n">response_type</span> <span class="o">=</span> <span class="s2">"code"</span>                             <span class="c1">## The response_type always has to be "code"</span>
<span class="n">state</span> <span class="o">=</span> <span class="s2">"sample"</span>                                   <span class="c1">##  The state field here acts as a session manager. you will be sent with the state field after successfull generation of auth_code </span>


<span class="c1">### Connect to the sessionModel object here with the required input parameters</span>
<span class="n">appSession</span> <span class="o">=</span> <span class="n">fyersModel</span><span class="o">.</span><span class="n">SessionModel</span><span class="p">(</span><span class="n">client_id</span> <span class="o">=</span> <span class="n">client_id</span><span class="p">,</span> <span class="n">redirect_uri</span> <span class="o">=</span> <span class="n">redirect_uri</span><span class="p">,</span><span class="n">response_type</span><span class="o">=</span><span class="n">response_type</span><span class="p">,</span><span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span><span class="n">secret_key</span><span class="o">=</span><span class="n">secret_key</span><span class="p">,</span><span class="n">grant_type</span><span class="o">=</span><span class="n">grant_type</span><span class="p">)</span>

<span class="c1"># ## Make  a request to generate_authcode object this will return a login url which you need to open in your browser from where you can get the generated auth_code </span>
<span class="n">generateTokenUrl</span> <span class="o">=</span> <span class="n">appSession</span><span class="o">.</span><span class="n">generate_authcode</span><span class="p">()</span>

<span class="sd">"""There are two method to get the Login url if  you are not automating the login flow</span>
<span class="sd">1. Just by printing the variable name </span>
<span class="sd">2. There is a library named as webbrowser which will then open the url for you without the hasel of copy pasting</span>
<span class="sd">both the methods are mentioned below"""</span>
<span class="nb">print</span><span class="p">((</span><span class="n">generateTokenUrl</span><span class="p">))</span>  
<span class="n">webbrowser</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">generateTokenUrl</span><span class="p">,</span><span class="n">new</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="sd">"""</span>
<span class="sd">run the code firstly upto this after you generate the auth_code comment the above code and start executing the below code """</span>
<span class="c1">##########################################################################################################################</span>

<span class="c1">### After succesfull login the user can copy the generated auth_code over here and make the request to generate the accessToken </span>
<span class="n">auth_code</span> <span class="o">=</span> <span class="s2">"Paste the auth_code generated from the first request"</span>
<span class="n">appSession</span><span class="o">.</span><span class="n">set_token</span><span class="p">(</span><span class="n">auth_code</span><span class="p">)</span>
<span class="n">response</span> <span class="o">=</span> <span class="n">appSession</span><span class="o">.</span><span class="n">generate_token</span><span class="p">()</span>

<span class="c1">## There can be two cases over here you can successfully get the acccessToken over the request or you might get some error over here. so to avoid that have this in try except block</span>
<span class="k">try</span><span class="p">:</span> 
    <span class="n">access_token</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"access_token"</span><span class="p">]</span>
<span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="p">,</span><span class="n">response</span><span class="p">)</span>  <span class="c1">## This will help you in debugging then and there itself like what was the error and also you would be able to see the value you got in response variable. instead of getting key_error for unsuccessfull response.</span>



<span class="c1">## Once you have generated accessToken now we can call multiple trading related or data related apis after that in order to do so we need to first initialize the fyerModel object with all the requried params.</span>
<span class="sd">"""</span>
<span class="sd">fyerModel object takes following values as arguments</span>
<span class="sd">1. accessToken : this is the one which you received from above </span>
<span class="sd">2. client_id : this is basically the app_id for the particular app you logged into</span>
<span class="sd">"""</span>
<span class="n">fyers</span> <span class="o">=</span> <span class="n">fyersModel</span><span class="o">.</span><span class="n">FyersModel</span><span class="p">(</span><span class="n">token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span><span class="n">is_async</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span><span class="n">client_id</span><span class="o">=</span><span class="n">client_id</span><span class="p">,</span><span class="n">log_path</span><span class="o">=</span><span class="s2">""</span><span class="p">)</span>


<span class="c1">## After this point you can call the relevant apis and get started with</span>

<span class="c1">####################################################################################################################</span>
<span class="sd">"""</span>
<span class="sd">1. User Apis : This includes (Profile,Funds,Holdings)</span>
<span class="sd">"""</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">get_profile</span><span class="p">())</span>  <span class="c1">## This will provide us with the user related data </span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">funds</span><span class="p">())</span>        <span class="c1">## This will provide us with the funds the user has </span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">holdings</span><span class="p">())</span>    <span class="c1">## This will provide the available holdings the user has </span>


<span class="c1">########################################################################################################################</span>

<span class="sd">"""</span>
<span class="sd">2. Transaction Apis : This includes (Tradebook,Orderbook,Positions)</span>
<span class="sd">"""</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">tradebook</span><span class="p">())</span>   <span class="c1">## This will provide all the trade related information </span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">orderbook</span><span class="p">())</span>   <span class="c1">## This will provide the user with all the order realted information </span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">positions</span><span class="p">())</span>   <span class="c1">## This will provide the user with all the positions the user has on his end </span>


<span class="c1">######################################################################################################################</span>

<span class="sd">"""</span>
<span class="sd">3. Order Placement  : This Apis helps to place order. </span>
<span class="sd">There are two ways to place order </span>
<span class="sd">a. single order : wherein you can fire one order at a time </span>
<span class="sd">b. multi order : this is used to place a basket of order but the basket size can max be 10 symbols</span>
<span class="sd">"""</span>

<span class="c1">## SINGLE ORDER </span>

<span class="n">data</span> <span class="o">=</span>  <span class="p">{</span>
      <span class="s2">"symbol"</span><span class="p">:</span><span class="s2">"NSE:ONGC-EQ"</span><span class="p">,</span>
      <span class="s2">"qty"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
      <span class="s2">"type"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
      <span class="s2">"side"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
      <span class="s2">"productType"</span><span class="p">:</span><span class="s2">"INTRADAY"</span><span class="p">,</span>
      <span class="s2">"limitPrice"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>
      <span class="s2">"stopPrice"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>
      <span class="s2">"validity"</span><span class="p">:</span><span class="s2">"DAY"</span><span class="p">,</span>
      <span class="s2">"disclosedQty"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>
      <span class="s2">"offlineOrder"</span><span class="p">:</span><span class="kc">False</span><span class="p">,</span>
      <span class="s2">"stopLoss"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>
      <span class="s2">"takeProfit"</span><span class="p">:</span><span class="mi">0</span>
    <span class="p">}</span>                              <span class="c1">## This is a sample example to place a limit order you can make the further changes based on your requriements </span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">place_order</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>

<span class="c1">## MULTI ORDER </span>

<span class="n">data</span> <span class="o">=</span> <span class="p">[{</span> <span class="s2">"symbol"</span><span class="p">:</span><span class="s2">"NSE:SBIN-EQ"</span><span class="p">,</span>
  <span class="s2">"qty"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
  <span class="s2">"type"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>  
  <span class="s2">"side"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span> 
  <span class="s2">"productType"</span><span class="p">:</span><span class="s2">"INTRADAY"</span><span class="p">,</span>   
  <span class="s2">"limitPrice"</span><span class="p">:</span><span class="mi">61050</span><span class="p">,</span>
  <span class="s2">"stopPrice"</span><span class="p">:</span><span class="mi">0</span> <span class="p">,</span>
  <span class="s2">"disclosedQty"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span> 
  <span class="s2">"validity"</span><span class="p">:</span><span class="s2">"DAY"</span><span class="p">,</span> 
  <span class="s2">"offlineOrder"</span><span class="p">:</span><span class="kc">False</span><span class="p">,</span> 
  <span class="s2">"stopLoss"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>  
  <span class="s2">"takeProfit"</span><span class="p">:</span><span class="mi">0</span>
<span class="p">},</span>
<span class="p">{</span>
  <span class="s2">"symbol"</span><span class="p">:</span><span class="s2">"NSE:HDFC-EQ"</span><span class="p">,</span>
  <span class="s2">"qty"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
  <span class="s2">"type"</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span>  
  <span class="s2">"side"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span> 
  <span class="s2">"productType"</span><span class="p">:</span><span class="s2">"INTRADAY"</span><span class="p">,</span>   
  <span class="s2">"limitPrice"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>
  <span class="s2">"stopPrice"</span><span class="p">:</span><span class="mi">0</span> <span class="p">,</span>
  <span class="s2">"disclosedQty"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span> 
  <span class="s2">"validity"</span><span class="p">:</span><span class="s2">"DAY"</span><span class="p">,</span> 
  <span class="s2">"offlineOrder"</span><span class="p">:</span><span class="kc">False</span><span class="p">,</span> 
  <span class="s2">"stopLoss"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>  
  <span class="s2">"takeProfit"</span><span class="p">:</span><span class="mi">0</span>
<span class="p">}]</span>                                                <span class="c1">### This takes input as a list containing multiple single order data into it and the execution of the orders goes in the same format as mentioned.</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">place_basket_orders</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>


<span class="c1">###################################################################################################################</span>

<span class="sd">"""</span>
<span class="sd">4. Other Transaction : This includes (modify_order,exit_position,cancel_order,convert_positions)</span>
<span class="sd">"""</span>

<span class="c1">## Modify_order request </span>
<span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
          <span class="s2">"id"</span><span class="p">:</span><span class="s2">"7574657627567"</span><span class="p">,</span> 
          <span class="s2">"type"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span> 
          <span class="s2">"limitPrice"</span><span class="p">:</span> <span class="mi">61049</span><span class="p">,</span>
          <span class="s2">"qty"</span><span class="p">:</span><span class="mi">1</span>
      <span class="p">}</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">modify_order</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>

<span class="c1">## Modify Multi Order </span>

<span class="n">data</span> <span class="o">=</span> <span class="p">[</span>
    <span class="p">{</span> <span class="s2">"id"</span><span class="p">:</span><span class="s2">"8102710298291"</span><span class="p">,</span>
  <span class="s2">"type"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
  <span class="s2">"limitPrice"</span><span class="p">:</span> <span class="mi">61049</span><span class="p">,</span>
  <span class="s2">"qty"</span><span class="p">:</span><span class="mi">0</span>
<span class="p">},</span>
<span class="p">{</span>
  <span class="s2">"id"</span><span class="p">:</span><span class="s2">"8102710298292"</span><span class="p">,</span>
  <span class="s2">"type"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
  <span class="s2">"limitPrice"</span><span class="p">:</span> <span class="mi">61049</span><span class="p">,</span>
  <span class="s2">"qty"</span><span class="p">:</span><span class="mi">1</span> 
<span class="p">}]</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">modify_basket_orders</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>


<span class="c1">### Cancel_order</span>
<span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"id"</span><span class="p">:</span><span class="s1">'808058117761'</span><span class="p">}</span>
<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">cancel_order</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>

<span class="c1">### cancel_multi_order </span>
<span class="n">data</span>  <span class="o">=</span>  <span class="p">[</span>
<span class="p">{</span> 
   <span class="s2">"id"</span><span class="p">:</span><span class="s1">'808058117761'</span>
 <span class="p">},</span>
 <span class="p">{</span>
   <span class="s2">"id"</span><span class="p">:</span><span class="s1">'808058117762'</span>
 <span class="p">}]</span>
 
<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">cancel_basket_orders</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>


<span class="c1">### Exit Position </span>
<span class="n">data</span>  <span class="o">=</span> <span class="p">{</span>
     <span class="s2">"id"</span><span class="p">:</span><span class="s2">"NSE:SBIN-EQ-INTRADAY"</span>
   <span class="p">}</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">exit_positions</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>


<span class="c1">### Convert Position</span>

<span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
     <span class="s2">"symbol"</span><span class="p">:</span><span class="s2">"MCX:SILVERMIC20NOVFUT"</span><span class="p">,</span>
     <span class="s2">"positionSide"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
     <span class="s2">"convertQty"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
     <span class="s2">"convertFrom"</span><span class="p">:</span><span class="s2">"INTRADAY"</span><span class="p">,</span>
     <span class="s2">"convertTo"</span><span class="p">:</span><span class="s2">"CNC"</span>
   <span class="p">}</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">convert_position</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>


<span class="c1">#################################################################################################################</span>

<span class="sd">"""</span>
<span class="sd">DATA APIS : This includes following Apis(History,Quotes,MarketDepth)</span>
<span class="sd">"""</span>

<span class="c1">## Historical Data </span>

<span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"symbol"</span><span class="p">:</span><span class="s2">"NSE:SBIN-EQ"</span><span class="p">,</span><span class="s2">"resolution"</span><span class="p">:</span><span class="s2">"D"</span><span class="p">,</span><span class="s2">"date_format"</span><span class="p">:</span><span class="s2">"0"</span><span class="p">,</span><span class="s2">"range_from"</span><span class="p">:</span><span class="s2">"1622097600"</span><span class="p">,</span><span class="s2">"range_to"</span><span class="p">:</span><span class="s2">"1622097685"</span><span class="p">,</span><span class="s2">"cont_flag"</span><span class="p">:</span><span class="s2">"1"</span><span class="p">}</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">history</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>

<span class="c1">## Quotes </span>

<span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"symbols"</span><span class="p">:</span><span class="s2">"NSE:SBIN-EQ"</span><span class="p">}</span>
<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">quotes</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>


<span class="c1">## Market Depth </span>

<span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"symbol"</span><span class="p">:</span><span class="s2">"NSE:SBIN-EQ"</span><span class="p">,</span><span class="s2">"ohlcv_flag"</span><span class="p">:</span><span class="s2">"1"</span><span class="p">}</span>
<span class="nb">print</span><span class="p">(</span><span class="n">fyers</span><span class="o">.</span><span class="n">depth</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
</pre>
    <h2>Getting started with Data Socket</h2>
    <pre
      lang="python3"
    ><span class="kn">from</span> <span class="nn">fyers_apiv3.FyersWebsocket</span> <span class="kn">import</span> <span class="n">data_ws</span>


<span class="k">def</span> <span class="nf">onmessage</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to handle incoming messages from the FyersDataSocket WebSocket.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        message (dict): The received message from the WebSocket.</span>

<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Response:"</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">onerror</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to handle WebSocket errors.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        message (dict): The error message received from the WebSocket.</span>


<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Error:"</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">onclose</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to handle WebSocket connection close events.</span>
<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Connection closed:"</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">onopen</span><span class="p">():</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to subscribe to data type and symbols upon WebSocket connection.</span>

<span class="sd">    """</span>
    <span class="c1"># Specify the data type and symbols you want to subscribe to</span>
    <span class="n">data_type</span> <span class="o">=</span> <span class="s2">"SymbolUpdate"</span>
    <span class="c1"># data_type = "DepthUpdate"</span>


    <span class="c1"># Subscribe to the specified symbols and data type</span>
    <span class="n">symbols</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'NSE:SBIN-EQ'</span><span class="p">,</span> <span class="s1">'NSE:ADANIENT-EQ'</span><span class="p">]</span>
    <span class="n">fyers</span><span class="o">.</span><span class="n">subscribe</span><span class="p">(</span><span class="n">symbols</span><span class="o">=</span><span class="n">symbols</span><span class="p">,</span> <span class="n">data_type</span><span class="o">=</span><span class="n">data_type</span><span class="p">)</span>

    <span class="c1"># Keep the socket running to receive real-time data</span>
    <span class="n">fyers</span><span class="o">.</span><span class="n">keep_running</span><span class="p">()</span>


<span class="c1"># Replace the sample access token with your actual access token obtained from Fyers</span>
<span class="n">access_token</span> <span class="o">=</span> <span class="s2">"XCXXXXXXM-100:eyJ0tHfZNSBoLo"</span>

<span class="c1"># Create a FyersDataSocket instance with the provided parameters</span>
<span class="n">fyers</span> <span class="o">=</span> <span class="n">data_ws</span><span class="o">.</span><span class="n">FyersDataSocket</span><span class="p">(</span>
    <span class="n">access_token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span>       <span class="c1"># Access token in the format "appid:accesstoken"</span>
    <span class="n">log_path</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span>                     <span class="c1"># Path to save logs. Leave empty to auto-create logs in the current directory.</span>
    <span class="n">litemode</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>                  <span class="c1"># Lite mode disabled. Set to True if you want a lite response.</span>
    <span class="n">write_to_file</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>              <span class="c1"># Save response in a log file instead of printing it.</span>
    <span class="n">reconnect</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>                  <span class="c1"># Enable auto-reconnection to WebSocket on disconnection.</span>
    <span class="n">on_connect</span><span class="o">=</span><span class="n">onopen</span><span class="p">,</span>               <span class="c1"># Callback function to subscribe to data upon connection.</span>
    <span class="n">on_close</span><span class="o">=</span><span class="n">onclose</span><span class="p">,</span>                <span class="c1"># Callback function to handle WebSocket connection close events.</span>
    <span class="n">on_error</span><span class="o">=</span><span class="n">onerror</span><span class="p">,</span>                <span class="c1"># Callback function to handle WebSocket errors.</span>
    <span class="n">on_message</span><span class="o">=</span><span class="n">onmessage</span>             <span class="c1"># Callback function to handle incoming messages from the WebSocket.</span>
<span class="p">)</span>

<span class="c1"># Establish a connection to the Fyers WebSocket</span>
<span class="n">fyers</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
</pre>
    <h2>Getting started with Order Socket</h2>
    <pre
      lang="python3"
    ><span class="kn">from</span> <span class="nn">fyers_apiv3.FyersWebsocket</span> <span class="kn">import</span> <span class="n">order_ws</span>


<span class="k">def</span> <span class="nf">onTrade</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to handle incoming messages from the FyersDataSocket WebSocket.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        message (dict): The received message from the WebSocket.</span>

<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Trade Response:"</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">onOrder</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to handle incoming messages from the FyersDataSocket WebSocket.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        message (dict): The received message from the WebSocket.</span>

<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Order Response:"</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">onPosition</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to handle incoming messages from the FyersDataSocket WebSocket.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        message (dict): The received message from the WebSocket.</span>

<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Position Response:"</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">onGeneral</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to handle incoming messages from the FyersDataSocket WebSocket.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        message (dict): The received message from the WebSocket.</span>

<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"General Response:"</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">onerror</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to handle WebSocket errors.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        message (dict): The error message received from the WebSocket.</span>


<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Error:"</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">onclose</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to handle WebSocket connection close events.</span>
<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Connection closed:"</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">onopen</span><span class="p">():</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Callback function to subscribe to data type and symbols upon WebSocket connection.</span>

<span class="sd">    """</span>
    <span class="c1"># Specify the data type and symbols you want to subscribe to</span>
    <span class="c1"># data_type = "OnOrders"</span>
    <span class="c1"># data_type = "OnTrades"</span>
    <span class="c1"># data_type = "OnPositions"</span>
    <span class="c1"># data_type = "OnGeneral"</span>
    <span class="n">data_type</span> <span class="o">=</span> <span class="s2">"OnOrders,OnTrades,OnPositions,OnGeneral"</span>

    <span class="n">fyers</span><span class="o">.</span><span class="n">subscribe</span><span class="p">(</span><span class="n">data_type</span><span class="o">=</span><span class="n">data_type</span><span class="p">)</span>

    <span class="c1"># Keep the socket running to receive real-time data</span>
    <span class="n">fyers</span><span class="o">.</span><span class="n">keep_running</span><span class="p">()</span>


<span class="c1"># Replace the sample access token with your actual access token obtained from Fyers</span>
<span class="n">access_token</span> <span class="o">=</span> <span class="s2">"XCXXXXXXM-100:eyJ0tHfZNSBoLo"</span>

<span class="c1"># Create a FyersDataSocket instance with the provided parameters</span>
<span class="n">fyers</span> <span class="o">=</span> <span class="n">order_ws</span><span class="o">.</span><span class="n">FyersOrderSocket</span><span class="p">(</span>
    <span class="n">access_token</span><span class="o">=</span><span class="n">access_token</span><span class="p">,</span>  <span class="c1"># Your access token for authenticating with the Fyers API.</span>
    <span class="n">write_to_file</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>        <span class="c1"># A boolean flag indicating whether to write data to a log file or not.</span>
    <span class="n">log_path</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span>                <span class="c1"># The path to the log file if write_to_file is set to True (empty string means current directory).</span>
    <span class="n">on_connect</span><span class="o">=</span><span class="n">onopen</span><span class="p">,</span>          <span class="c1"># Callback function to be executed upon successful WebSocket connection.</span>
    <span class="n">on_close</span><span class="o">=</span><span class="n">onclose</span><span class="p">,</span>           <span class="c1"># Callback function to be executed when the WebSocket connection is closed.</span>
    <span class="n">on_error</span><span class="o">=</span><span class="n">onerror</span><span class="p">,</span>           <span class="c1"># Callback function to handle any WebSocket errors that may occur.</span>
    <span class="n">on_general</span><span class="o">=</span><span class="n">onGeneral</span><span class="p">,</span>       <span class="c1"># Callback function to handle general events from the WebSocket.</span>
    <span class="n">on_orders</span><span class="o">=</span><span class="n">onOrder</span><span class="p">,</span>          <span class="c1"># Callback function to handle order-related events from the WebSocket.</span>
    <span class="n">on_positions</span><span class="o">=</span><span class="n">onPosition</span><span class="p">,</span>    <span class="c1"># Callback function to handle position-related events from the WebSocket.</span>
    <span class="n">on_trades</span><span class="o">=</span><span class="n">onTrade</span>           <span class="c1"># Callback function to handle trade-related events from the WebSocket.</span>
<span class="p">)</span>

<span class="c1"># Establish a connection to the Fyers WebSocket</span>
<span class="n">fyers</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
</pre>
  </div>
</div>
